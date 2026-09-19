#!/usr/bin/env python3
"""Compute scenario returns from explicit same-currency user inputs; no data fetching."""

import argparse
import json
import math
import sys
from pathlib import Path


def number(value, field, minimum=None, strictly_positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{field} must be finite")
    if strictly_positive and value <= 0:
        raise ValueError(f"{field} must be positive")
    if minimum is not None and value < minimum:
        raise ValueError(f"{field} must be at least {minimum}")
    return value


def calculate(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a JSON object")
    entry = number(data.get("entry"), "entry", strictly_positive=True)
    years = number(data.get("horizon_years"), "horizon_years", strictly_positive=True)
    dividends = number(data.get("dividends", 0), "dividends", minimum=0)
    costs = number(data.get("costs_per_share", 0), "costs_per_share", minimum=0)
    stop = data.get("stop")
    if stop is not None:
        stop = number(stop, "stop", minimum=0)
        if stop >= entry:
            raise ValueError("stop must be below entry")
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        raise ValueError("scenarios must be a nonempty list")
    rows, weights, names = [], [], set()
    for i, case in enumerate(scenarios):
        if not isinstance(case, dict):
            raise ValueError(f"scenario {i} must be an object")
        name = case.get("name")
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError("Each scenario must have a unique nonempty name")
        names.add(name)
        has_target = "target" in case
        has_eps_pe = "eps" in case or "pe" in case
        if has_target == has_eps_pe:
            raise ValueError(f"{name}: supply either target or eps and pe")
        if has_target:
            target = number(case["target"], f"{name}.target", minimum=0)
        else:
            eps = number(case.get("eps"), f"{name}.eps", minimum=0)
            pe = number(case.get("pe"), f"{name}.pe", strictly_positive=True)
            target = eps * pe
        terminal_value = target + dividends - costs
        if not math.isfinite(terminal_value) or terminal_value < 0:
            raise ValueError(f"{name}: terminal value must be finite and nonnegative")
        total_return = terminal_value / entry - 1
        annualized = (terminal_value / entry) ** (1 / years) - 1
        if not math.isfinite(annualized):
            raise ValueError(f"{name}: annualized return is not finite")
        row = {"name": name, "target": target, "total_return": total_return,
               "annualized_scenario_return": annualized}
        if stop is not None and target > entry:
            row["technical_reward_risk_before_costs"] = (target - entry) / (entry - stop)
        if "probability" in case:
            weight = number(case["probability"], f"{name}.probability", minimum=0)
            if weight > 1:
                raise ValueError(f"{name}: probability must be at most 1")
            row["probability"] = weight
            weights.append(weight)
        rows.append(row)
    if weights and (len(weights) != len(rows) or not math.isclose(sum(weights), 1, abs_tol=1e-8)):
        raise ValueError("Supply all probabilities summing to 1, or omit all probabilities")
    result = {"entry": entry, "horizon_years": years, "dividends": dividends,
              "costs_per_share": costs, "scenarios": rows,
              "units": "Returns are decimals; prices and cash flows share one currency",
              "assumptions": "Cash dividends and costs aggregated at horizon; no reinvestment, FX or tax model"}
    if weights:
        result["expected_total_return"] = sum(r["probability"] * r["total_return"] for r in rows)
    if stop is not None:
        result["stop"] = stop
        result["stop_price_change"] = stop / entry - 1
        result["stop_limitation"] = "Execution can gap or slip; this is not maximum loss"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = calculate(json.loads(args.input.read_text(encoding="utf-8")))
        print(json.dumps(result, indent=2, allow_nan=False))
    except (OSError, ValueError, OverflowError) as exc:
        print(f"Invalid scenario input: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
