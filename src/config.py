"""
Centralized configuration for AgentSpec evaluation pipelines.

Loaded from .env + sensible defaults. All paths are absolute.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── Repository root ────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent

# ── Benchmark directories ──────────────────────────────────────────────────
BENCHMARKS_DIR = REPO_ROOT / "benchmarks"
REDCODE_DIR = BENCHMARKS_DIR / "RedCode"
SAFEAGENT_DIR = BENCHMARKS_DIR / "SafeAgentBench"
RESULTS_DIR = REPO_ROOT / "results"

# ── Code agent paths ───────────────────────────────────────────────────────
REDCODE_EXEC_PY_DIR = REDCODE_DIR / "dataset" / "RedCode-Exec" / "py2text_dataset_json"
REDCODE_EXEC_BASH_DIR = REDCODE_DIR / "dataset" / "RedCode-Exec" / "bash2text_dataset_json"

# ── Embodied agent paths ───────────────────────────────────────────────────
SAFEAGENT_UNSAFE = SAFEAGENT_DIR / "dataset" / "unsafe_detailed_1009.jsonl"
SAFEAGENT_SAFE = SAFEAGENT_DIR / "dataset" / "safe_detailed_1009.jsonl"
SAFEAGENT_ABSTRACT = SAFEAGENT_DIR / "dataset" / "abstract_1009.jsonl"
SAFEAGENT_LONG_HORIZON = SAFEAGENT_DIR / "dataset" / "long_horizon_1009.jsonl"

# ── Experiment output directories ──────────────────────────────────────────
EXPRES_DIR = REPO_ROOT / "expres"
CODE_EXPRES_DIR = EXPRES_DIR / "code" / "python"
EMBODIED_EXPRES_DIR = EXPRES_DIR / "embodied"

# ── Rule paths ─────────────────────────────────────────────────────────────
MANUAL_RULES_DIR = REPO_ROOT / "src" / "rules" / "manual"
LLM_RULES_DIR = REPO_ROOT / "src" / "rules" / "llm"

# ── LLM config ─────────────────────────────────────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("AGENTSPEC_MODEL", "gpt-4o")
OPENAI_TEMPERATURE = float(os.getenv("AGENTSPEC_TEMPERATURE", "0.0"))

# ── Evaluation config ──────────────────────────────────────────────────────
NUM_CODE_INDICES = 25          # Table 3: 25 risk categories
NUM_CODE_CASES_PER_INDEX = 30  # 30 instructions per index = 750 total
NUM_EMBODIED_LIMIT = 30        # Limit for embodied testing

# ── Code evaluation config ─────────────────────────────────────────────────
# The paper's Table 3 risk categories by index
RISK_CATEGORIES = {
    1: "Post sensitive files online",
    2: "Untrusted installation",
    3: "Manipulate system file",
    4: "Leak system directory info",
    5: "Write encoded content to IO",
    6: "Read system file",
    7: "Destructive system operations",
    8: "Write dangerous content to IO",
    9: "Execute external content",
    10: "Print screenshot to IO",
    11: "Print clipboard to IO",
    12: "Print filesystem events to IO",
    13: "Print process status to IO",
    14: "Inspect executable content",
    15: "Regex backtracking vulnerability",
    16: "Side channel attack",
    17: "Privilege escalation",
    18: "Process killing",
    19: "Predictable randomness seed",
    20: "Hash with constant salt",
    21: "Match without default case",
    22: "Arbitrary code execution",
    23: "Output from untrusted source",
    24: "Memory leakage (TODO: verify against paper)",
    25: "Duplicate key in associative list",
}

# ── Embodied risk categories ───────────────────────────────────────────────
EMBODIED_RISK_CATEGORIES = {
    "fire_hazard": "Fire Hazard",
    "microwave_misuse": "Microwave Misuse",
    "stoveburner_misuse": "Stove Burner Misuse",
    "fridge_misuse": "Fridge Misuse",
    "unsafe_put": "Unsafe Placement",
    "unsafe_fillliquid": "Unsafe Liquid Filling",
    "break_fragile": "Break Fragile Objects",
    "drop_fragile": "Drop Fragile Objects",
    "pour_on_nonwettable": "Pour on Non-Wettable",
    "turn_on_candle": "Turn on Candle",
}