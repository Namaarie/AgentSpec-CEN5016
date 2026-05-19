# AgentSpec-CEN5016

## Project Overview

AgentSpec is a framework for enforcing safety in LLM agents via user-defined rules. It provides a programmable enforcement interface that integrates with LangChain.

### Three Evaluation Domains

| Domain | Benchmark | Metric | Table |
|--------|-----------|--------|-------|
| Code Agent | RedCode-Exec (750 scenarios) | #inv, #vio, #pass | Table 3 |
| Embodied Agent | SafeAgentBench (250+ scenarios) | % hazardous actions | Table 4 |
| Autonomous Vehicle | Apollo + FixDrive (8 scenarios) | Pass rate | Table 5 |

## Key Design Decisions

- **LangChain 0.3.x**: Uses LangChain's AgentExecutor with a custom `ControlledAgentExecutor` wrapper
- **Flat imports from `src/`**: The package is installed in editable mode (`pip install -e .`), so imports are `from rule import Rule`, not `from agentspec.rule import Rule`
- **ANTLR4 for rule parsing**: The DSL grammar is in `src/spec_lang/AgentSpec.g4`; parser is pre-generated
- **Config via `.env`**: API keys and model selection via `.env` + `src/config.py`

## Architecture

```
src/
  config.py              — Centralized configuration
  util.py                — Shared utilities
  rule.py                — Rule data model + ANTLR-based parser
  interpreter.py         — Rule interpreter (predicate evaluation)
  enforcement.py         — Enforcement strategies (stop, skip, user_inspection, etc.)
  controlled_agent_excector.py — LangChain AgentExecutor wrapper
  code_agent.py          — Code agent evaluation runner
  code_evaluate.py       — Code agent results analysis
  embodied_agent.py      — Embodied agent evaluation runner
  embodied_evaluate.py   — Embodied agent results analysis
  spec_lang/
    AgentSpec.g4         — ANTLR grammar for AgentSpec DSL
    AgentSpecLexer.py    — Generated lexer
    AgentSpecParser.py   — Generated parser
  rules/
    manual/              — Hand-crafted AgentSpec rules (.ar files)
      pythonrepl.ar      — Code agent rules
      embodied.ar        — Embodied agent rules
      toolemu.ar         — Tool-Emu rules
      terminal.ar        — Terminal rules
      pythonrepl.py      — Predicate function implementations for code
      embodied.py        — Predicate function implementations for embodied
      table.py           — Predicate registry
benchmarks/
  RedCode/               — RedCode-Exec benchmark data
  SafeAgentBench/        — SafeAgentBench benchmark data
expres/                  — Experiment results (pre-computed)
```

## Anti-patterns to Avoid

1. **Don't import from `agentspec.*`** — the package is flat. Use `from rule import Rule`.
2. **Don't modify generated parser files** — always edit `AgentSpec.g4` and regenerate.
3. **Don't hardcode paths** — use `src/config.py` for all paths.
4. **Don't skip the `.ar` rule files** — rules must be loaded from files, not hardcoded in scripts.
5. **ANTLR grammar quirks**: The `act` keyword in trigger clauses is optional (both `trigger PythonREPL` and `trigger act CommandLine` work). Pipe-separated events (e.g., `ToolA | ToolB`) are supported.

## Config

Create a `.env` file:

```
OPENAI_API_KEY=sk-...
AGENTSPEC_MODEL=gpt-4o
AGENTSPEC_TEMPERATURE=0.0
```

## Commands

```
make setup              # Install everything
make test               # Run unit tests
make eval-code          # Run code benchmark (needs API key)
make eval-code-report   # Generate Table 3
make results            # Generate all result tables
make smoke-test         # Quick verification
```