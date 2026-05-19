.PHONY: help setup eval-code eval-code-report eval-embodied eval-embodied-report \
        eval-all results clean smoke-test regenerated-parser

help:
	@echo "AgentSpec Evaluation Commands:"
	@echo ""
	@echo "  make setup              - Install dependencies + package"
	@echo "  make regenerate-parser  - Regenerate ANTLR parser from grammar"
	@echo "  make test               - Run unit tests"
	@echo ""
	@echo "  make eval-code          - Run code agent benchmark (Table 3)"
	@echo "  make eval-code-report   - Generate code results table"
	@echo "  make eval-embodied      - Run embodied agent benchmark (Table 4)"
	@echo "  make eval-embodied-report - Generate embodied results table"
	@echo ""
	@echo "  make eval-all           - Run all benchmarks"
	@echo "  make results            - Generate all result tables"
	@echo "  make smoke-test         - Verify pipeline without LLM calls"
	@echo "  make clean              - Remove experiment results"

setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirement.txt
	. .venv/bin/activate && pip install -e .

regenerate-parser:
	cd src/spec_lang && java -jar antlr-4.13.2-complete.jar \
		-Dlanguage=Python3 AgentSpec.g4

test:
	. .venv/bin/activate && python -m pytest src/ -v --tb=short

eval-code:
	. .venv/bin/activate && cd src && python code_agent.py

eval-code-report:
	mkdir -p results
	. .venv/bin/activate && python src/code_evaluate.py --output results/code_table3.md

eval-embodied:
	. .venv/bin/activate && cd src && python embodied_agent.py

eval-embodied-report:
	mkdir -p results
	. .venv/bin/activate && python src/embodied_evaluate.py --output results/embodied_table4.md

eval-all: eval-code eval-embodied

results: eval-code-report eval-embodied-report

smoke-test:
	@echo "=== AgentSpec Smoke Test ==="
	. .venv/bin/activate && python -c "from rule import Rule; print('1/5 imports OK')"
	. .venv/bin/activate && python -c "\
from rule import Rule; \
r = Rule.from_text('rule @test\ntrigger\n    act ShellTool\ncheck\n    is_destructive\nenforce\n    stop\nend'); \
assert r.id == 'test'; assert r.event == 'ShellTool'; print('2/5 rule parsing OK')"
	. .venv/bin/activate && python -c "\
from rules.manual.table import predicate_table; \
assert len(predicate_table) > 20; \
print(f'3/5 {len(predicate_table)} predicates OK')"
	. .venv/bin/activate && python -c "\
from config import REPO_ROOT, REDCODE_DIR, SAFEAGENT_DIR; \
print('4/5 config OK')"
	. .venv/bin/activate && python -c "\
from controlled_agent_excector import ControlledAgentExecutor; \
from rule import Rule; \
from enforcement import ENFORCEMENT_TO_CLASS; \
assert len(ENFORCEMENT_TO_CLASS) == 5; \
print('5/5 enforcement strategies OK')"
	@echo ""
	@echo "=== All smoke tests passed ==="

clean:
	rm -rf results/
	rm -f expres/code/python/*.jsonl
	rm -f expres/embodied/stat.jsonl
