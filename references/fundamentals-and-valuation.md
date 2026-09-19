# Expectations, earnings and value

## Event and earnings review

Build a compact actual/consensus/prior-guidance/updated-guidance comparison for decision-relevant metrics. Preserve GAAP versus adjusted definitions and fiscal/calendar years. State whether consensus is from before or after the release. Earnings quality matters: cash conversion, working capital, stock compensation, buybacks/share dilution, debt, one-offs and accounting changes.

Explain the price reaction with an expectation ladder: reported results → guidance → business KPIs → management narrative → valuation entering the event → positioning and market/sector move. Separate the initial release from subsequent call commentary. A beat can disappoint a higher expectation bar, and a miss can rally after worse fears were priced in. Distinguish published sell-side consensus from documented buy-side or informal expectations; label the latter unobserved if unavailable. Do not treat a post-event price move alone as proof of one cause.

For software, test AI monetization versus substitution using retention/churn, customer additions, seats versus usage, pricing, remaining obligations, margins, competition and compliance/mission-critical switching costs. Treat management's moat assertions as claims to test. For semiconductors, connect end-customer spending, product cadence, supply limits, margins and customer concentration; distinguish demand pulled forward from durable growth.

For AI applications/agents, examine users, paid conversion, revenue or transaction take rate, inference cost per task, subsidies and the path to positive unit economics. Lower token prices can shift demand between providers or expand usage; they do not automatically prove falling aggregate demand or revenue. Test whether a new entry point diverts incumbents' traffic or also generates incremental transactions. Distinguish recurring ARR, backlog and orders from recognized revenue, profit and cash.

Normalize organic versus acquisition-driven growth, constant-currency versus reported growth, nominal versus real demand, investment gains, one-off fees, stock compensation and capex accounting changes. Sparse disclosure or a reorganized reporting segment is a research clue, not proof of either confidence or failure. For a technology challenger, compare commercial readiness, throughput, yield/quality, total ownership cost and exposed product/geographic revenue; a prototype is not competitive volume production.

## Valuation discipline

Use the corpus's transparent forward EPS × justified P/E range when suitable. Show EPS source/vintage, fiscal year, adjusted/GAAP basis, growth, comparable companies and the reason for the multiple. Display near-year and following-year values separately. If a calendar/fiscal roll-forward expands the range, distinguish passage of time from an actual earnings upgrade.

Use sector-appropriate alternatives when P/E is uninformative: normalized mid-cycle earnings, EV/EBITDA or FCF, DCF, or book value/ROE for relevant financials. Bridge enterprise to equity value and account for debt, cash and share count. Do not use a generic technology P/E band for every business. Use diluted per-share forecasts consistently; avoid double counting buybacks. For cyclical memory/commodities, test peak versus mid-cycle earnings, spot/contract prices, capacity lead times and forecast downgrades beyond the peak year: low peak-earnings P/E can be expensive. If inputs are too unstable, give a sensitivity or withhold a point valuation.

Analyst targets and buy ratings are a comparison point, not independent proof of undervaluation. Historical peak prices, an analyst consensus or an unchanged old multiple cannot establish a floor. Stress lower earnings and a lower multiple together when justified. Explain what the current price implies about growth, margins or the multiple, and which assumption your variant view disputes.

Separate four quantities: historical cost basis; current market price; estimated fundamental value at a named horizon; tactical support/resistance. Evaluate adding versus trimming with prospective return and risk from today, not a desire to lower average cost or recover a loss. Consider capital tied up, alternative opportunities, taxes/fees only when applicable and specified, concentration and catalyst timing. An expensive stock can stay strong; a cheap stock can keep falling. A trim can reduce overlapping sector/customer exposure without expressing a bearish company thesis. Compare prospective trading gains with taxes, costs, missed upside and re-entry risk. For staged entries, specify total exposure/cash limits and the conditions for each tranche; an initial small position is no promise to keep adding.

Treat defensive business characteristics separately from defensive valuation. Reliable demand or strong pricing power does not make an expensive stock drawdown-proof. Cash or a suitable short-duration alternative can be an explicit benchmark when no stock offers enough margin of safety; source any stated yield and product terms.

## Scenario arithmetic

For scenarios with a common horizon H in years and the same valuation currency:

- Target price = EPS at horizon × terminal P/E (or independently derived target).
- Total return = (target + cash dividends − per-share round-trip costs) / entry − 1.
- Annualized scenario return = (1 + total return)^(1/H) − 1, with terminal receipt of cash flows assumed. Use dated cash-flow IRR when timing is material.
- Expected total return = sum(probability × scenario total return). Probabilities must be exhaustive, mutually exclusive and sum to 1.
- Annualizing expected terminal wealth is not an expected CAGR or a backtested outcome. Do not annualize a short tactical gain into a sustainable yearly promise.
- Technical reward/risk = (target − entry)/(entry − stop), only for stop < entry < target, before costs. A stop can gap or slip; it does not cap fundamental downside.

Probabilities are optional. Label judgmental weights; show sensitivity where the decision depends on them. Do not derive them from analyst-rating shares, option-implied volatility alone or vague similarity to past charts. For multi-currency portfolios, show local-currency return first and separately state FX assumptions; include actual relevant fees/tax assumptions without inventing them.

### Calculator

Run `python3 scripts/scenario_math.py INPUT.json` from this skill directory. Accept a common `entry`, positive `horizon_years`, optional nonnegative `dividends` and `costs_per_share`, optional `stop`, and a nonempty `scenarios` list. Each scenario needs `name`, either nonnegative `target` or nonnegative `eps` plus positive `pe`, and optional `probability` in [0,1]. Supply probabilities for all scenarios or none; if supplied they must sum to 1. All numeric assumptions use the same currency. The script emits calculations and rejects contradictory targets or invalid weights; it supplies no market data.

Example synthetic input: `{"entry":100,"horizon_years":1,"stop":90,"scenarios":[{"name":"bear","target":70,"probability":0.25},{"name":"base","eps":6,"pe":20,"probability":0.5},{"name":"bull","target":160,"probability":0.25}]}`. This is arithmetic demonstration, not a forecast.
