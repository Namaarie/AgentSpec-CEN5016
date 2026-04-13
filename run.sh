#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ANTLR_JAR="$ROOT_DIR/src/spec_lang/antlr-4.13.2-complete.jar"
PYTHON_BIN="${PYTHON_BIN:-python}"

if [ -f "$ROOT_DIR/.env" ]; then
	# shellcheck disable=SC1091
	source "$ROOT_DIR/.env"
fi

run_python() {
	if [ -x "$ROOT_DIR/.venv/Scripts/python.exe" ]; then
		"$ROOT_DIR/.venv/Scripts/python.exe" "$@"
	elif [ -x "$ROOT_DIR/.venv/bin/python" ]; then
		"$ROOT_DIR/.venv/bin/python" "$@"
	else
		"$PYTHON_BIN" "$@"
	fi
}

run_in_root() {
	(
		cd "$ROOT_DIR"
		"$@"
	)
}

run_java() {
	if command -v java >/dev/null 2>&1; then
		JAVA_CMD="$(command -v java)"
		JAVA_USES_WINDOWS_PATHS=0
	elif command -v java.exe >/dev/null 2>&1; then
		JAVA_CMD="$(command -v java.exe)"
		JAVA_USES_WINDOWS_PATHS=1
	elif [ -n "${JAVA_HOME:-}" ] && [ -x "$JAVA_HOME/bin/java" ]; then
		JAVA_CMD="$JAVA_HOME/bin/java"
		JAVA_USES_WINDOWS_PATHS=0
	elif [ -n "${JAVA_HOME:-}" ] && [ -x "$JAVA_HOME/bin/java.exe" ]; then
		JAVA_CMD="$JAVA_HOME/bin/java.exe"
		JAVA_USES_WINDOWS_PATHS=1
	else
		echo "Java is required for this option but was not found on PATH."
		return 1
	fi

	"$JAVA_CMD" "$@"
}

check_requirements() {
	echo "Checking environment..."

	if ! command -v "$PYTHON_BIN" >/dev/null 2>&1 && \
	   [ ! -x "$ROOT_DIR/.venv/Scripts/python.exe" ] && \
	   [ ! -x "$ROOT_DIR/.venv/bin/python" ]; then
		echo "Python is not available."
		exit 1
	fi

	if [ -f "$ROOT_DIR/requirement.txt" ]; then
		echo "Dependency file found: requirement.txt"
	elif [ -f "$ROOT_DIR/requirements.txt" ]; then
		echo "Dependency file found: requirements.txt"
	else
		echo "Warning: no requirements file found."
	fi

	# Validate core Python dependencies used by the smoke tests.
	if ! run_in_root run_python - <<'PY'
import importlib
import sys

required_modules = [
    "antlr4",
    "langchain",
    "langchain_core",
    "langchain_text_splitters",
    "langchain_openai",
    "langchain_community",
    "langchain_experimental",
]

missing = []
for module_name in required_modules:
	try:
		importlib.import_module(module_name)
	except Exception:
		missing.append(module_name)
if missing:
    print("Missing Python modules:", ", ".join(missing))
    print("Install dependencies with: pip install -r requirement.txt")
    sys.exit(1)
PY
	then
		echo "Dependency validation failed."
		return 1
	fi

	echo "Environment looks usable"
}

run_test_1() {
	echo "Running Test 1: LangChain smoke demo"
	run_in_root run_python -m src.spec_lang.demo_langchain_working || return 1
}

run_test_2() {
	echo "Running Test 2: Parser unit tests"
	run_in_root run_python -m unittest src.spec_lang.test_parse || return 1
}

run_test_3() {
	echo "Running Test 3: Parse inline rule - user inspection"
	run_in_root run_python - <<'PY' || return 1
from src.spec_lang.test_parse import parse

program = '''rule @check_shell_exec
trigger
    pythonrepl
check
    is_destructive
enforce
    user_inspection
end
'''
parse(program)
print("Parsed inline user_inspection rule")
PY
}

run_test_4() {
	echo "Running Test 4: Parse inline rule - stop enforcement"
	run_in_root run_python - <<'PY' || return 1
from src.spec_lang.test_parse import parse

program = '''rule @block_shell_exec
trigger
    pythonrepl
check
    is_destructive
enforce
    stop
end
'''
parse(program)
print("Parsed inline stop rule")
PY
}

run_test_5() {
	echo "Running Test 5: Controlled agent import smoke test"
	run_in_root run_python - <<'PY' || return 1
from src.spec_lang.controlled_agent_excector import initialize_controlled_agent

print("Import OK:", initialize_controlled_agent.__name__)
PY
}

run_test_6() {
	echo "Running Test 6: Manual predicate registry smoke test"
	run_in_root run_python - <<'PY' || return 1
from src.rules.manual.table import predicate_table

required = ["is_destructive"]
missing = [name for name in required if name not in predicate_table]
if missing:
	raise SystemExit(f"Missing predicates: {missing}")
print("Registered predicates available:", ", ".join(required))
PY
}

run_test_7() {
	echo "Running Test 7: Bytecode compilation smoke test"
	run_in_root run_python -m py_compile \
		src/spec_lang/demo_langchain_working.py \
		src/spec_lang/controlled_agent_excector.py \
		src/spec_lang/rule.py \
		src/rules/manual/pythonrepl.py \
		src/rules/manual/table.py || return 1
	echo "Compilation OK"
}

run_test_8() {
	local antlr_jar="./src/spec_lang/antlr-4.13.2-complete.jar"
	local grammar_file="./src/spec_lang/AgentSpec.g4"

	echo "Running Test 8: Regenerate parser from grammar"
	if [ ! -f "$ANTLR_JAR" ]; then
		echo "ANTLR jar not found at: $ANTLR_JAR"
		return 1
	fi
	run_in_root run_java -jar "$antlr_jar" -Dlanguage=Python3 "$grammar_file" || return 1
	echo "Parser regenerated"
}

run_test_9() {
	echo "Running Test 9: Full local smoke suite"
	run_test_2 || return 1
	run_test_5 || return 1
	run_test_6 || return 1
	run_test_7 || return 1
}

show_menu() {
	echo ""
	echo "=============================="
	echo "   AGENTSPEC ARTIFACT MENU"
	echo "=============================="
	echo " 1) LangChain smoke demo"
	echo " 2) Parser unit tests"
	echo " 3) Parse inline rule: user inspection"
	echo " 4) Parse inline rule: stop enforcement"
	echo " 5) Controlled agent import smoke test"
	echo " 6) Manual predicate registry smoke test"
	echo " 7) Bytecode compilation smoke test"
	echo " 8) Regenerate parser from grammar"
	echo " 9) Full local smoke suite"
	echo " 0) Exit"
	echo "=============================="
}

execute_choice() {
	local choice="$1"
	case "$choice" in
		"") return 0 ;;
		1) run_test_1 ;;
		2) run_test_2 ;;
		3) run_test_3 ;;
		4) run_test_4 ;;
		5) run_test_5 ;;
		6) run_test_6 ;;
		7) run_test_7 ;;
		8) run_test_8 ;;
		9) run_test_9 ;;
		0) echo "Exiting."; exit 0 ;;
		*) echo "Invalid option: $choice"; return 1 ;;
	esac
}

main() {
	check_requirements

	if [ $# -eq 1 ]; then
		execute_choice "$1"
		exit 0
	fi

	while true; do
		show_menu
		if ! read -r -p "Select a test (0-9): " choice; then
			echo "Exiting."
			exit 0
		fi
		if [ -z "$choice" ]; then
			continue
		fi
		if [ "$choice" = "0" ]; then
			echo "Exiting."
			exit 0
		fi
		if execute_choice "$choice"; then
			echo ""
			if [ -t 0 ]; then
				read -r -p "Press Enter to return to the menu..." _
			fi
		fi
	done
}

main "$@"