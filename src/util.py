"""
Shared utilities for AgentSpec evaluation pipelines.
"""

import json
import os
from langchain_core.agents import AgentAction
from config import MANUAL_RULES_DIR
from rule import Rule


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


def load_manual_rules(rules_dir=None):
    """Load all AgentSpec rules from .ar files in a directory.

    Each .ar file may contain multiple rules separated by 'rule @'.
    Returns a list of Rule objects.
    """
    if rules_dir is None:
        rules_dir = MANUAL_RULES_DIR
    rules_dir = str(rules_dir)

    rules = []
    for fname in sorted(os.listdir(rules_dir)):
        if not fname.endswith(".ar"):
            continue
        fpath = os.path.join(rules_dir, fname)
        with open(fpath) as f:
            content = f.read().strip()
        # Split on 'rule @' boundaries (re-join with prefix)
        segments = content.split("rule @")
        for seg in segments:
            seg = seg.strip()
            if not seg:
                continue
            rule_str = f"rule @{seg}"
            try:
                rule = Rule.from_text(rule_str)
                rules.append(rule)
            except Exception as e:
                # Skip rules that can't parse (comments, non-rule text)
                pass
    return rules


def load_code_data(index, data_dir=None):
    """Load a single risk-category index's 30-code dataset.

    Returns the parsed JSON list.
    """
    from config import REDCODE_EXEC_PY_DIR
    if data_dir is None:
        data_dir = str(REDCODE_EXEC_PY_DIR)
    fpath = os.path.join(data_dir, f"index{index}_30_codes_full.json")
    with open(fpath) as f:
        return json.loads(f.read())


def ensure_dir(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)