---
name: rhinofinance-market-analysis
description: Analyze stock markets, sectors, earnings and individual stocks using the RhinoFinance-corrected source collection. Use for RhinoFinance-style macro and policy transmission, expectations versus results, forward valuation, AI economics, institutional flows, price-volume analysis, portfolio risk, staged entries, stop-loss reviews and re-entry or replacement decisions. Adapt to US or other requested equity markets; do not use for generic financial definitions or trade execution.
---

# RhinoFinance Market Analysis

Reproduce the source collection's analytical architecture: connect the market regime and expectations to business fundamentals, valuation, positioning, chart structure, and a conditional action plan. Write original analysis in the user's language. Do not impersonate the presenter or copy their historical recommendations.

## Establish the decision

- Resolve security, exchange, currency, as-of date, trading session, horizon, and whether the question concerns a new position or an existing holding. Use the requested scope; default an unspecified market review to US equities, the corpus's principal market.
- Separate near-term timing (days/weeks), tactical holding (weeks/months), and fundamental valuation (typically 12–24 months). A long-term upside thesis does not imply an immediate rebound.
- For portfolio actions, use current user-supplied holdings and constraints or their authoritative current files. Do not import the presenter's cost basis, allocations, options, leverage, or trades. If portfolio size/cash is unknown, give a security-level view without inventing position quantities.
- Assess business quality and valuation independently of portfolio fit. Keep attractive candidates visible even when issuer, sector, geography or factor exposures overlap existing holdings. Present concentration separately with a supported loss assessment, sizing/staging and optional funding alternatives; concentration alone must not exclude a candidate. Honor explicit user hard limits.
- Choose full market review, stock/sector deep dive, earnings/catalyst review, or a short change update. Scale the work to the question; do not force a market-wide report for a focused question.

## Evidence standard

Browse or use available authenticated market sources for every current investment analysis. Record price date/time, session, currency, financial period and source vintage. Cite direct sources beside material factual claims. Use company filings/IR for business results, statistical agencies/central banks/Treasury for macro releases, exchange/provider data for prices and options, and dated identifiable research for estimates or positioning.

Treat the source transcripts as examples of reasoning, not independently verified facts. The refreshed source basis contains 255 transcripts and three correction/reference files, inspected on 2026-09-26. Read [source-method-map.md](references/source-method-map.md) for provenance and [source-quality.md](references/source-quality.md) when interpreting transcripts or refreshing the corpus. Text correction is not audio verification or a financial fact check. Keep filename date, spoken US session date and upload time separate. Do not carry old levels, probabilities, forecasts or reported events into current analysis without verification.

Label observed facts, management guidance, consensus estimates, third-party models, own calculations and own judgment distinctly. State unavailable inputs and proceed with a bounded conclusion. Never fabricate proprietary CTA levels, dealer gamma, institutional flows, consensus estimates or historical success rates. A citation to a transcript supports only that its author said something.

For exact source lookup or another corpus refresh, use [source-catalog.json](references/source-catalog.json); search by filename, video URL, stable index or method tags rather than loading it for routine analysis.

## Analysis workflow

1. **Describe the tape.** Compare major indices, equal-weight/breadth, leaders/laggards, sectors, rates and volatility. Identify whether the move is broad participation, concentration, rotation, a mechanical event, or inconclusive. Read [market-and-flows.md](references/market-and-flows.md) for market reviews and macro/flow questions.
2. **Explain the expectations gap.** Ask what was expected before the event, what changed, and how earnings/cash flows or discount rates transmit that change to equity prices. Distinguish good results from results good enough for the price. Diagnose multiple compression, business disruption, financing stress, earnings deterioration and possible forced selling separately; require evidence for each. Read [fundamentals-and-valuation.md](references/fundamentals-and-valuation.md) for stock, sector and earnings analysis.
3. **Estimate value with explicit assumptions.** Show the fiscal period, earnings basis and justified multiple range, or a more suitable sector model. Separate consensus from an independently reasoned case. Show downside as well as upside, and expose the assumptions that make an apparently cheap stock a value trap.
4. **Assess the path and timing.** Test current price/volume, relative strength, support/resistance zones and confirmation/invalidation conditions. Read [price-volume-and-events.md](references/price-volume-and-events.md). A price chart cannot establish intrinsic value or the identity/motive of buyers.
5. **Translate to action.** Select buy/add/hold/wait/trim/exit or insufficient evidence, and state why it dominates the relevant alternatives at today's price. Distinguish a tactical stop, portfolio loss limit and fundamental thesis break. For holdings, staged entries, stops, re-entry, replacements or drawdown questions, read [portfolio-risk-and-reentry.md](references/portfolio-risk-and-reentry.md). Separate core and tactical exposure, quantify current portfolio loss under a common stress where possible, and define what changes a wait/hold decision.
6. **Update the thesis.** State what changed versus an available dated prior analysis, what did not, and whether a previous condition triggered, failed or expired. Retrieve prior analysis only when a comparison is requested or materially needed. Never silently move a failed target or treat a price bounce as thesis validation.

## Decision output

Read [report-formats.md](references/report-formats.md) and choose the smallest useful format. Lead with the conclusion and horizon, then supporting evidence and uncertainties. For substantive stock recommendations include a compact decision table with: current price/as-of; catalyst; valuation range; technical trigger; downside/invalidation; preferred action; alternative action; next review.

Use a bear/base/bull table when a forward-return decision needs it. Include probabilities only when a defensible basis exists and label judgmental probabilities as subjective; sum to 100%. Do not equate analyst-rating percentages with probabilities. Calculate prospective returns from current or proposed entry price, separately from the holder's unrealized gain/loss. Do not represent a technical stop as a maximum possible loss.

Use `scripts/scenario_math.py` for repeatable scenario/return arithmetic when helpful; its input contract and formulas are in [fundamentals-and-valuation.md](references/fundamentals-and-valuation.md). It computes supplied assumptions and does not source data or validate their economic plausibility. For options-implied event ranges, IPO/lockup mechanics, financing guarantees or credit-risk read-throughs, read only the applicable section of [special-situations.md](references/special-situations.md).

## Completion check

- Reconcile tickers, units, fiscal years, adjusted versus GAAP earnings, and price dates.
- Keep fundamentals, valuation, flows, technicals and action mutually coherent while explaining disagreements.
- Make shock-based valuations conditional on both magnitude and duration. A ceasefire headline, a legal ruling or a chart breakout does not by itself prove restored supply, implemented policy or repaired business fundamentals.
- Check related-party financing, customer payments and physical delivery constraints when translating AI demand or backlog into supplier earnings. Avoid counting the same financed expenditure repeatedly as independent final demand.
- Treat crowding, seasonality, overbought RSI, analyst targets and historical analogues as conditional evidence, not deterministic timing rules.
- Avoid hindsight, cherry-picked event samples and unverified claims of market manipulation or secret information.
- Make the recommendation falsifiable and distinguish facts from forecasts. Do not default reflexively to hold or force a trade when evidence is weak.
- Distinguish an absolute gain, profit above an estimated fair-value band and actual benchmark-relative excess return. Record realized losses, failed setups and missed re-entry risk without rewriting the original plan.
- Create files or update a tracker only when requested or useful to the requested deliverable; use the available file workflow. The skill does not authorize orders, messages, subscriptions or scheduled tasks.
