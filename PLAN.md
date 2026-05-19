# AgentSpec Reproducibility Plan

> **For Hermes:** Use subagent-driven-development to implement this plan task-by-task.

**Goal:** Transform the AgentSpec-CEN5016 repo into a reproducible benchmark suite that can verify the paper's results from Tables 3, 4, 5, and 6 — with simple one-command entry points.

**Architecture:** Three self-contained evaluation pipelines (Code, Embodied, AV) sharing a common AgentSpec rule engine, with proper config management, Makefile orchestration, and output collectors that produce paper-format tables.

**Tech Stack:** Python 3.12, LangChain 0.3.x, ANTLR4, python-dotenv, pytest, AI2-THOR (embodied), Docker (RedCode-Exec containers)

---

## Phase 0: Audit & Fix Core Infrastructure (pre-work, mostly done)

### 0.1 Verify Current State

**Objective:** Confirm the existing fixes actually work end-to-end.

**Files:** `src/` (all .py files), `pyproject.toml`, `requirement.txt`

**Step 1: Run full import test**

```bash
cd ~/research/AgentSpec-CEN5016
source .venv/bin/activate
python -c "
from rule import Rule; from interpreter import RuleInterpreter
from controlled_agent_excector import initialize_controlled_agent
from spec_lang.AgentSpecLexer import AgentSpecLexer
from rules.manual.table import predicate_table
print(f'OK - {len(predicate_table)} predicates loaded')
"
```

**Step 2: Run unit tests**

```bash
python -m pytest src/ -v --tb=short 2>&1 | head -40
```

**Step 3: Check for remaining broken imports**

```bash
# Check each Python file has valid imports
python -c "
import ast, os, sys
errors = []
for root, dirs, files in os.walk('src'):
    for f in files:
        if f.endswith('.py') and f != '__init__.py':
            path = os.path.join(root, f)
            try:
                with open(path) as fh:
                    ast.parse(fh.read())
            except SyntaxError as e:
                errors.append((path, str(e)))
print(f'{len(errors)} syntax errors' if errors else 'All files parse cleanly')
"
```

---

## Phase 1: Fix ANTLR Grammar & Parser

The current grammar (`src/spec_lang/AgentSpec.g4`) has several issues:
- The `enforceClause` rule expects `enforce` followed by enforcement tokens (no `(` needed), but the generated parser code has `ENFORCE LPAREN` — mismatch.
- The trigger clause doesn't support `act ToolName` syntax used in examples.
- Line 23-24 in the template has `{{` and `}}` (jinja-style escaping) instead of `{` and `}`.
- The template's `triggerClause` uses `toolkit DOT tool` but the actual code's `triggerClause` uses just `event`.

### Task 1.1: Audit the grammar file

**Objective:** Identify every mismatch between the grammar and the actual rule format used in `src/rules/manual/*.ar` and `src/spec_lang/rule_examples/*.ar`.

**Files:**
- Read: `src/spec_lang/AgentSpec.g4`
- Read: `src/rules/manual/pythonrepl.ar`
- Read: `src/rules/manual/embodied.ar`
- Read: `src/spec_lang/rule_examples/conflict_light_status.ar`
- Read: `src/rules/manual/toolemu.ar`

**Step 1: Extract all unique rule formats**

```bash
cd ~/research/AgentSpec-CEN5016/src/rules/manual
cat embodied.ar pythonrepl.ar terminal.ar toolemu.ar \
  ../../spec_lang/rule_examples/*.ar | grep -v "^$" | head -80
```

**Step 2: Map to grammar rules**

Document which grammar productions each rule exercises.

### Task 1.2: Regenerate the parser from the grammar

**Objective:** Generate fresh `AgentSpecLexer.py` and `AgentSpecParser.py` from the grammar.

**Files:**
- Create: `scripts/regenerate_parser.sh`

**Step 1: Write regeneration script**

```bash
#!/bin/bash
# scripts/regenerate_parser.sh
set -e
cd "$(dirname "$0")/../src/spec_lang"
JAR="antlr-4.13.2-complete.jar"
GRAMMAR="AgentSpec.g4"

java -jar "$JAR" -Dlanguage=Python3 "$GRAMMAR"
echo "Parser regenerated successfully"
```

**Step 2: Run it**

```bash
bash scripts/regenerate_parser.sh
```

**Step 3: Verify the output files exist**

- `src/spec_lang/AgentSpecLexer.py`
- `src/spec_lang/AgentSpecParser.py`
- `src/spec_lang/AgentSpecListener.py`
- `src/spec_lang/AgentSpec.interp`
- `src/spec_lang/AgentSpec.tokens`

### Task 1.3: Fix grammar if needed

**Objective:** If the grammar doesn't match the rule files, fix the grammar.

Look for:
- `enforceClause` needing parentheses → the original grammar has `ENFORCE enforcement+` (no parens), but the generated parser might expect `LPAREN`. Check the generated code.
- `triggerClause` needing `act` keyword support
- Any missing PREDICATE entries vs what's in `predicate_table`

---

## Phase 2: Build Code Agent Evaluation Pipeline

The paper's Table 3 evaluates the Code Agent on RedCode-Exec: 25 risk categories × 30 risky instructions = 750 scenarios. Metrics: #inv (invocations), #vio (violations caught), #pass (allowed by user).

### Task 2.1: Create centralized config

**Objective:** Single config file for API keys, model names, and paths.

**Create:** `src/config.py`

**Step 1: Write config module**

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Paths
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCHMARKS_DIR = os.path.join(REPO_ROOT, "benchmarks")
REDCODE_DIR = os.path.join(BENCHMARKS_DIR, "RedCode")
SAFEAGENT_DIR = os.path.join(BENCHMARKS_DIR, "SafeAgentBench")
EXPRES_DIR = os.path.join(REPO_ROOT, "expres")

# LLM config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("AGENTSPEC_MODEL", "gpt-4o")
OPENAI_TEMPERATURE = float(os.getenv("AGENTSPEC_TEMPERATURE", "0.0"))

# Data paths
REDCODE_EXEC_PY_DIR = os.path.join(
    REDCODE_DIR, "dataset", "RedCode-Exec", "py2text_dataset_json"
)
REDCODE_EXEC_BASH_DIR = os.path.join(
    REDCODE_DIR, "dataset", "RedCode-Exec", "bash2text_dataset_json"
)
SAFEAGENT_UNSAFE = os.path.join(SAFEAGENT_DIR, "dataset", "unsafe_detailed_1009.jsonl")
SAFEAGENT_SAFE = os.path.join(SAFEAGENT_DIR, "dataset", "safe_detailed_1009.jsonl")
```

### Task 2.2: Fix code_agent.py for proper batch evaluation

**Objective:** Fix the broken script so it runs all 750 scenarios properly (not break on first iteration).

**Modify:** `src/code_agent.py`

**Issues to fix:**
1. Line 60: `break` after first case — removes it so loop runs all 30 cases per index
2. Hardcoded dataset paths — use config module
3. No progress reporting — add tqdm or simple counter
4. Rule loading is missing — currently passes `rules=[]`, need to load the manual rules
5. The `proc_intermediate_step` is duplicated from `code_agent.py` to `embodied_agent.py` — extract to `src/util.py`

**New structure:**

```
src/
  config.py          (NEW) - central config
  util.py            (NEW) - shared utilities (proc_intermediate_step, etc.)
  code_agent.py      (FIX) - clean evaluation runner
  code_evaluate.py   (NEW) - evaluates results against rules
```

**Step 1: Create `src/util.py`**

```python
from langchain_core.agents import AgentAction

def proc_intermediate_step(steps):
    """Convert LangChain intermediate steps to serializable dicts."""
    res = []
    for step in steps:
        if not step:
            continue
        if isinstance(step[0], AgentAction):
            res.append({
                "action": {"tool": step[0].tool, "input": step[0].tool_input},
                "observation": step[1]
            })
        else:
            raise ValueError(f"Unknown step type: {type(step[0])}")
    return res
```

**Step 2: Refactor `code_agent.py`**

Key changes to the `execute()` and `run()` functions:
- Remove the `break` on line 60
- Load rules from `src/rules/manual/` using proper config paths
- Add `tqdm` progress bar
- Add CSV/JSONL output with structured metrics

### Task 2.3: Create code evaluation analysis script

**Objective:** Compute the paper's Table 3 metrics from experiment results.

**Create:** `src/code_evaluate.py`

**Step 1: Write evaluation logic**

```python
#!/usr/bin/env python3
"""
Evaluates code agent experiment results against AgentSpec rules.
Computes: #inv (invocations), #vio (rule violations), #pass (user-allowed).
Corresponds to paper Table 3.
"""

from pathlib import Path
import json
import sys

def evaluate_index(index: int, results_dir: str, rules_dir: str):
    """
    For a given risk category index:
    - Count #inv: agent attempted to invoke PythonREPL
    - Count #vio: code tripped AgentSpec rules
    - Count #pass: code was allowed after user inspection
    """
    # Implementation loads results JSONL, applies rules, tabulates
    pass

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Evaluate code agent results")
    parser.add_argument("--results-dir", default="expres/code/python/")
    parser.add_argument("--rules-dir", default="src/rules/manual/")
    parser.add_argument("--output", default=None, help="Output table path")
    args = parser.parse_args()
    
    # Tabulate results across all 25 risk categories
    print("ID | Risk Category | #inv | #vio | #pass")
    print("---|---------------|------|------|------")
    # ... loop 1..25 and print rows

if __name__ == "__main__":
    main()
```

### Task 2.4: Create Makefile entry point

**Objective:** Single command runs the full code benchmark.

**Create/Makefile:** Add:

```makefile
# Code Agent benchmark
.PHONY: eval-code
eval-code:
	cd src && python code_agent.py

.PHONY: eval-code-report
eval-code-report:
	cd src && python code_evaluate.py --output ../results/code_table3.md
```

---

## Phase 3: Build Embodied Agent Evaluation Pipeline

The paper's Table 4 evaluates the Embodied Agent on SafeAgentBench: 10 unsafe + 1 safe categories. Metrics: % tasks leading to hazards without vs with AgentSpec.

The embodied agent uses AI2-THOR which is already installed in the venv. But it needs a running X server / display.

### Task 3.1: Fix embodied_agent.py for batch evaluation

**Modify:** `src/embodied_agent.py`

**Issues to fix:**
1. Reads `runned` set from a previous results file (resume logic) — make configurable
2. Hardcoded limits (i = 1..30, not runned all) — parameterize
3. Error handling swallows exceptions — need better logging
4. Scene management needs reset per instruction
5. Hardcoded rule list — should load from config

### Task 3.2: Create embodied evaluation analysis

**Create:** `src/embodied_evaluate.py`

**Logic:**
- Load experiment results from `expres/embodied/`
- For each risk category, compute % hazardous actions with/without AgentSpec
- Table format matches paper Table 4

### Task 3.3: Add Makefile entry for embodied

```makefile
.PHONY: eval-embodied
eval-embodied:
	cd src && python embodied_agent.py

.PHONY: eval-embodied-report
eval-embodied-report:
	cd src && python embodied_evaluate.py --output ../results/embodied_table4.md
```

---

## Phase 4: LLM-Generated Rule Evaluation

The paper's Table 6 evaluates LLM-generated rules (OpenAI o1) across all three domains. The generation scripts are in `src/gen.py` and `src/rules/llm/generate.py`.

### Task 4.1: Fix LLM rule generation pipeline

**Modify:** `src/rules/llm/generate.py`

**Issues:**
- Uses hardcoded file paths
- No progress tracking
- Hardcoded LLM model

**Changes:**
- Use config module for API keys and model
- Add OpenAI o1 model support
- Save generated rules with metadata

### Task 4.2: Create LLM evaluation script

**Create:** `src/llm_evaluate.py`

**Logic:**
- Load LLM-generated rules
- Apply to RedCode-Exec and SafeAgentBench test sets
- Compute enforcement rate (Table 6)
- Compute precision and recall for embodied

```makefile
.PHONY: eval-llm-rules
eval-llm-rules:
	cd src && python rules/llm/generate.py

.PHONY: eval-llm-report
eval-llm-report:
	cd src && python llm_evaluate.py --output ../results/llm_table6.md
```

---

## Phase 5: Run Scripts, AGENTS.md, and Makefile

### Task 5.1: Create top-level Makefile

**Create:** `Makefile`

```makefile
.PHONY: help setup eval-all eval-code eval-embodied clean

help:
	@echo "AgentSpec Evaluation Commands:"
	@echo "  make setup          - Install dependencies + package"
	@echo "  make eval-code      - Run code agent benchmark (Table 3)"
	@echo "  make eval-embodied  - Run embodied agent benchmark (Table 4)"
	@echo "  make eval-all       - Run all benchmarks"
	@echo "  make results        - Generate all result tables"
	@echo "  make clean          - Remove experiment results"

setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirement.txt
	. .venv/bin/activate && pip install -e .

eval-code:
	. .venv/bin/activate && cd src && python code_agent.py

eval-embodied:
	. .venv/bin/activate && cd src && python embodied_agent.py

results:
	mkdir -p results
	. .venv/bin/activate && python src/code_evaluate.py --output results/code_table3.md
	. .venv/bin/activate && python src/embodied_evaluate.py --output results/embodied_table4.md

clean:
	rm -rf src/expres/code/python/*.jsonl
	rm -rf src/expres/embodied/*.jsonl
	rm -rf results/
```

### Task 5.2: Create AGENTS.md

**Create:** `AGENTS.md`

Contents:
- Project architecture overview
- Three evaluation domains (Code, Embodied, AV)
- Key design decisions (LangChain 0.3.x, flat imports from src/)
- Anti-patterns to avoid
- Config via `.env` and `src/config.py`
- ANTLR grammar quirks (pre-existing issues with `act` keyword)

### Task 5.3: Update README.md

The existing README has a usage section (line 34-75) that references `controlled_agent_excector` and `demo_langchain()`. Update it with:
- Evaluation command reference
- Expected outputs / papers tables
- `.env` configuration example
- Tips for running RedCode in Docker (reference the RedCode README)

---

## Phase 6: Documentation & Verification

### Task 6.1: Verify code agent results match paper

Create a script that:
1. Runs code agent on a single risk category (e.g., index 1, "Post sensitive files online")
2. Computes #inv, #vio, #pass
3. Reports if results are in expected ballpark from Table 3:
   - index 1: #inv=14, #vio=14, #pass=0

### Task 6.2: Verify embodied agent results match paper

Create a verification script that:
1. Runs embodied agent on a single unsafe scenario
2. Checks that hazardous action is prevented with AgentSpec
3. Reports hazard rate with/without AgentSpec

### Task 6.3: Create smoke test

```bash
#!/bin/bash
# test/smoke.sh - verifies the entire pipeline without calling LLMs
echo "=== AgentSpec Smoke Test ==="
source .venv/bin/activate

# Test imports
python -c "from rule import Rule; print('1/5 imports OK')"

# Test rule parsing
python -c "
from rule import Rule
r = Rule.from_text('rule @test\ntrigger ShellTool\ncheck is_destructive\nenforce stop\nend')
assert r.id == 'test'
assert r.event == 'ShellTool'
print('2/5 rule parsing OK')
"

# Test predicate table loaded
python -c "
from rules.manual.table import predicate_table
assert len(predicate_table) > 20
print(f'3/5 {len(predicate_table)} predicates OK')
"

# Test config
python -c "
from config import REPO_ROOT, REDCODE_DIR, SAFEAGENT_DIR
assert REPO_ROOT.endswith('AgentSpec-CEN5016')
print('4/5 config OK')
"

# Test basic agent instantiation
python -c "
from controlled_agent_excector import ControlledAgentExecutor
from rule import Rule
from enforcement import ENFORCEMENT_TO_CLASS
assert len(ENFORCEMENT_TO_CLASS) == 5
print('5/5 enforcement strategies OK')
"

echo "=== All smoke tests passed ==="
```

---

## Appendix: Paper Experiment Details for Reference

### Table 3: Code Agent Results

| ID | Risk Category | #inv | #vio | #pass |
|----|--------------|------|------|-------|
| 1 | Post sensitive files online | 14 | 14 | 0 |
| 2 | Untrusted installation | 21 | 21 | 0 |
| ... | (25 categories total) | | | |
| 25 | Duplicate key in associative list | 0 | 0 | 0 |

Uses RedCode-Exec py2text dataset (750 scenarios). Agent = CodeAct/ReAct with PythonREPL.

### Table 4: Embodied Agent Results

| Category | w/out | with |
|----------|-------|------|
| Fire Hazard | 28.57% | 0% |
| ... (10 unsafe + 1 safe) | | |

Uses SafeAgentBench (250 unsafe + safe scenarios). Agent = ReAct with robotic controller + AI2-THOR.

### Table 5: AV Results

8 law-breaking scenarios. 100% pass rate with manual rules. Uses FixDrive scenarios on Apollo.

### Table 6: LLM-Generated Rules

| Agent | #Scenario | #Example | #Rule | Enforced % |
|-------|-----------|----------|-------|------------|
| Code | 750 | 75 | 25 | 87.26% |
| Embodied | 250 | 25 | 10 | 95.56% |
| AV | 8 | 0 | 6 | 62.50% |

LLM = OpenAI o1 with few-shot in-context examples.