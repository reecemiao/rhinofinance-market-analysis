---
name: rhinofinance-market-analysis
description: Analyze stock markets, sectors, earnings and individual stocks using the framework distilled from the RhinoFinance-corrected transcripts. Use for RhinoFinance-style market reviews, macro-to-equity transmission, expectations versus results, valuation, institutional positioning, price-volume interpretation, and conditional buy/add/hold/trim/exit decisions. Adapt to US or other requested equity markets; do not use for generic financial definitions or trade execution.
---

# RhinoFinance Market Analysis

Reproduce the source collection's analytical architecture: connect the market regime and expectations to business fundamentals, valuation, positioning, chart structure, and a conditional action plan. Write original analysis in the user's language. Do not impersonate the presenter or copy their historical recommendations.

## Establish the decision

- Resolve security, exchange, currency, as-of date, trading session, horizon, and whether the question concerns a new position or an existing holding. Use the requested scope; default an unspecified market review to US equities, the corpus's principal market.
- Separate near-term timing (days/weeks), tactical holding (weeks/months), and fundamental valuation (typically 12–24 months). A long-term upside thesis does not imply an immediate rebound.
- For portfolio actions, use current user-supplied holdings and constraints or their authoritative current files. Do not import the presenter's cost basis, allocations, options, leverage, or trades. If portfolio size/cash is unknown, give a security-level view without inventing position quantities.
- Choose full market review, stock/sector deep dive, earnings/catalyst review, or a short change update. Scale the work to the question; do not force a market-wide report for a focused question.

## Evidence standard

Browse or use available authenticated market sources for every current investment analysis. Record price date/time, session, currency, financial period and source vintage. Cite direct sources beside material factual claims. Use company filings/IR for business results, statistical agencies/central banks/Treasury for macro releases, exchange/provider data for prices and options, and dated identifiable research for estimates or positioning.

Treat the source transcripts as examples of reasoning, not independently verified facts. Their correction notes explicitly leave some numbers, tickers, dates and missing chart references unresolved. The filename date can differ from the spoken US session date. Do not carry their old levels, probabilities, forecasts or reported events into a current analysis without verification. Read [source-method-map.md](references/source-method-map.md) for provenance and retrieval guidance.

Label observed facts, management guidance, consensus estimates, third-party models, own calculations and own judgment distinctly. State unavailable inputs and proceed with a bounded conclusion. Never fabricate proprietary CTA levels, dealer gamma, institutional flows, consensus estimates or historical success rates. A citation to a transcript supports only that its author said something.

## Analysis workflow

1. **Describe the tape.** Compare major indices, equal-weight/breadth, leaders/laggards, sectors, rates and volatility. Identify whether the move is broad participation, concentration, rotation, a mechanical event, or inconclusive. Read [market-and-flows.md](references/market-and-flows.md) for market reviews and macro/flow questions.
2. **Explain the expectations gap.** Ask what was expected before the event, what changed, and how earnings/cash flows or discount rates transmit that change to equity prices. Distinguish good results from results good enough for the price. Read [fundamentals-and-valuation.md](references/fundamentals-and-valuation.md) for stock, sector and earnings analysis.
3. **Estimate value with explicit assumptions.** Show the fiscal period, earnings basis and justified multiple range, or a more suitable sector model. Separate consensus from an independently reasoned case. Show downside as well as upside, and expose the assumptions that make an apparently cheap stock a value trap.
4. **Assess the path and timing.** Test current price/volume, relative strength, support/resistance zones and confirmation/invalidation conditions. Read [price-volume-and-events.md](references/price-volume-and-events.md). A price chart cannot establish intrinsic value or the identity/motive of buyers.
5. **Translate to action.** Select buy/add/hold/wait/trim/exit or insufficient evidence, and state why it dominates the relevant alternatives at today's price. Distinguish a tactical stop from a fundamental thesis break. If waiting or holding, define the event/price/evidence that changes the decision and when to review it.
6. **Update the thesis.** State what changed versus an available dated prior analysis, what did not, and whether a previous condition triggered, failed or expired. Retrieve prior analysis only when a comparison is requested or materially needed. Never silently move a failed target or treat a price bounce as thesis validation.

## Decision output

Read [report-formats.md](references/report-formats.md) and choose the smallest useful format. Lead with the conclusion and horizon, then supporting evidence and uncertainties. For substantive stock recommendations include a compact decision table with: current price/as-of; catalyst; valuation range; technical trigger; downside/invalidation; preferred action; alternative action; next review.

Use a bear/base/bull table when a forward-return decision needs it. Include probabilities only when a defensible basis exists and label judgmental probabilities as subjective; sum to 100%. Do not equate analyst-rating percentages with probabilities. Calculate prospective returns from current or proposed entry price, separately from the holder's unrealized gain/loss. Do not represent a technical stop as a maximum possible loss.

Use `scripts/scenario_math.py` for repeatable scenario/return arithmetic when helpful; its input contract and formulas are in [fundamentals-and-valuation.md](references/fundamentals-and-valuation.md). It computes supplied assumptions and does not source data or validate their economic plausibility. For options-implied event ranges, IPO/lockup mechanics, financing guarantees or credit-risk read-throughs, read only the applicable section of [special-situations.md](references/special-situations.md).

## Completion check

- Reconcile tickers, units, fiscal years, adjusted versus GAAP earnings, and price dates.
- Keep fundamentals, valuation, flows, technicals and action mutually coherent while explaining disagreements.
- Treat crowding, seasonality, overbought RSI, analyst targets and historical analogues as conditional evidence, not deterministic timing rules.
- Avoid hindsight, cherry-picked event samples and unverified claims of market manipulation or secret information.
- Make the recommendation falsifiable and distinguish facts from forecasts. Do not default reflexively to hold or force a trade when evidence is weak.
- Create files or update a tracker only when requested or useful to the requested deliverable; use the available file workflow. The skill does not authorize orders, messages, subscriptions or scheduled tasks.
