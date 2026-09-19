# RhinoFinance Market Analysis

A reusable agent skill for evidence-based stock-market, sector, earnings, and individual-stock analysis, distilled from the RhinoFinance-corrected transcript collection.

## Use

Ask a compatible skill-enabled assistant:

> Use $rhinofinance-market-analysis to analyze the US stock market and my selected stocks, with current evidence, valuation scenarios, price-volume signals, and clear action triggers.

For a focused review, specify the ticker, exchange, analysis date, investment horizon, and whether you already hold the stock. Current analysis requires fresh, cited market and company data.

## Contents

- `SKILL.md`: workflow and evidence standards.
- `references/`: macro and flows, fundamentals and valuation, price-volume interpretation, report formats, special situations, and source provenance.
- `scripts/scenario_math.py`: calculator for supplied scenario assumptions; see the input contract in `references/fundamentals-and-valuation.md`.
- `agents/openai.yaml` and `assets/icon.svg`: assistant display metadata.

## Install

Copy this repository's skill files together into your assistant's supported skills directory under `rhinofinance-market-analysis`, preserving the relative paths. Follow that assistant's skill installation instructions.

## Provenance and limits

The framework was distilled from 99 corrected transcripts. The repository contains analytical guidance and a source catalog, not the original transcript collection. Private Google Drive links have been removed from this public export; public video references are retained.

Historical transcript statements are not verified market facts. The skill requires fresh evidence, explicit assumptions, downside scenarios, and falsifiable decision conditions. It does not execute trades or guarantee investment results.
