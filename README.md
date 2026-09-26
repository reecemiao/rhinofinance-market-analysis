# RhinoFinance Market Analysis

A reusable agent skill for evidence-based stock-market, sector, earnings, and individual-stock analysis, distilled from the RhinoFinance-corrected source collection.

## Use

Ask a compatible skill-enabled assistant:

> Use $rhinofinance-market-analysis to analyze the US stock market and my selected stocks, with current evidence, valuation scenarios, price-volume signals, and clear action triggers.

For a focused review, specify the ticker, exchange, analysis date, investment horizon, and whether you already hold the stock. For portfolio decisions, provide current holdings, cash, and risk constraints. Current analysis requires fresh, cited market and company data.

## Contents

- `SKILL.md`: workflow and evidence standards.
- `references/`: macro and flows, fundamentals and valuation, AI economics, price-volume interpretation, portfolio risk, staged entries, stop-loss and re-entry decisions, report formats, special situations, and source provenance.
- `references/source-catalog.json`: the complete 258-file source inventory with stable indices, public video references, content hashes, method tags, and review provenance.
- `references/source-quality.md`: correction limits, unresolved source uncertainty, and the corpus refresh process.
- `scripts/scenario_math.py`: calculator for supplied scenario assumptions; see the input contract in `references/fundamentals-and-valuation.md`.
- `agents/openai.yaml` and `assets/icon.svg`: assistant display metadata.

## Install

Copy this repository's skill files together into your assistant's supported skills directory under `rhinofinance-market-analysis`, preserving the relative paths. Follow that assistant's skill installation instructions.

## Provenance and limits

Updated on 2026-09-26 from all 258 files in the corrected source collection: 255 transcripts and three correction/reference documents. Transcript filename dates span 2025-08-30 through 2026-09-23. The refresh retains the original 99 transcript indices and adds 156 transcripts plus the three auxiliary documents.

All files were retrieved with byte-size reconciliation. Review comprised a full-text thematic scan of every transcript, selected-passage and chronological-sequence review, and full review of the auxiliary documents. This was not an audio audit or sentence-by-sentence factual validation.

The repository contains analytical guidance and a source catalog, not the original transcript collection. Private Google Drive links and file/folder IDs have been removed from this public export; public video references are retained.

Historical transcript statements are not verified market facts. The skill requires fresh evidence, explicit assumptions, downside scenarios, and falsifiable decision conditions. Portfolio concentration is assessed separately from a security's investment merit. The skill does not execute trades or guarantee investment results.
