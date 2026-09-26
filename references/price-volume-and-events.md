# Technical structure and event behavior

## Reproducible technical context

Use verified OHLCV data with source, exchange timezone, trading-session cutoffs and consistent split/dividend adjustments. Do not mix after-hours quotes with regular-session daily candles or compare a partial day's volume with full-day averages. Distinguish price-return and total-return series.

Describe trend with higher/lower highs and lows, relevant moving averages, volatility and support/resistance zones tied to observed pivots, gaps or consolidation. Use a zone rather than invented precision. Record timeframe, current price relative to zone, confirmation criterion, invalidation and next objective. If a transcript refers to an unseen chart, its exact level/construction cannot be recovered by guesswork.

Distinguish left-side entry near a defensible valuation/support zone before a reversal from right-side entry after breakout/retest confirmation. Discuss the cost-versus-confirmation tradeoff. A wick through resistance differs from a close above it; a close above differs from a sustained breakout with participation. Define confirmation appropriate to the timeframe rather than forcing the same two-day rule everywhere.

Compare volume with an explicitly defined trailing baseline that excludes the event day. Use relative strength against a relevant sector and benchmark, and assess follow-through, reversals and gap holds/fills. Greater volume can reflect distribution, covering, mechanical rebalancing or new demand; it does not identify the buyer. Treat price-level volume profiles as provider/algorithm-dependent and require source data before claiming overhead trapped positions.

For RSI or divergence, state timeframe/lookback and specify which price and indicator pivots diverge. Overbought can persist and divergence can resolve through sideways time or price correction; it does not make a pullback inevitable or determine its timing. Do not invent numerical RSI from a narrative or screenshot without enough information. Additional indicators such as Bollinger bands or sequential counts need disclosed parameters and sufficient input data; correlated indicators are not independent probability evidence. Separate daily timing from weekly/monthly structure.

Separate a halt in the decline, a temporary rebound, a confirmed trend reversal and long-run mean reversion. Specify observable conditions for each. After a break, compare follow-through and volume with what the bearish hypothesis predicted; rapid recovery and poor follow-through can justify a failed-break hypothesis pending confirmation. Former support can become resistance. A steep trendline with few pivots, an old untouched price level or a recently listed stock offers weaker structural evidence. For a weak stock that appears cheap, require a reason the thesis and expected payoff compensate for the path risk; do not mechanically average down. For strong but expensive stocks, consider expected return, position concentration and planned trims without claiming a precise top.

## Price/volume after catalysts

When asked for historical event behavior, assemble an inspectable, reproducible event sample rather than anecdotal charts:

1. Define comparable event types, sample period, universe and inclusion rules before calculating results. Include disappointing and successful events, not just memorable winners.
2. Confirm exact announcement times. Map premarket events to that trading session, after-close events to the next, and holidays/weekends to the next eligible session. Use the last unaffected regular close as the event-return baseline.
3. Separate pre-event drift, opening gap, open-to-close reaction and subsequent +1/+5/+20-session returns. Use split-adjusted prices and a stated benchmark adjustment. Define whether event-day return is included in each cumulative measure.
4. Calculate event relative volume against a prior-session average or median; control for earnings, expiry, index rebalances and unrelated simultaneous news. If intraday evidence is unavailable, state that gap and intraday decomposition cannot be established.
5. Report sample count, median, dispersion, hit rate and drawdown/adverse excursion where data permit. Distinguish touching a level at any time within five sessions from closing beyond it on session five. Preserve corrections to earlier statistics and recalculate percentage arithmetic. Mark small samples, overlap, regime differences and missing data. Historical frequency is not the present trade's probability.
6. Link the present setup to comparable fundamentals/expectations and market regime. Present plausible scenarios and confirmation triggers; do not claim an inferred causal effect from an observational event study.

## Action mechanics

Specify entry zone or condition, thesis, holding horizon, catalyst/review date, profit-taking criterion, and a tactical invalidation or fundamental exit rule. Define whether a stop uses intraday breach or closing confirmation. Show prospective reward/risk where inputs are defensible, but do not infer expected profitability from this ratio without probabilities. Beta is sensitivity, not maximum downside. Discuss gap risk and separate investment thesis management from a short-term trading setup.

When a setup expires or fails, say so. A fresh pattern can justify a new plan with a new rationale; do not retrospectively redefine the old plan to call it successful. Respect the user's execution constraints, including minimum holding periods and permitted instruments.

Use a dated state sequence when following a recovery: falling → possible stabilization → rebound into resistance → confirmed breakout/retest, or renewed failure. State the observable condition for each transition and how new pivots change the levels. Do not skip from one strong session to a proven long-term bottom. A bullish sector ETF does not establish that every constituent has repaired its own structure. Simultaneous software and semiconductor strength is possible; do not force a permanent rotation narrative. Source anchors: 205, 215, 218, 223, 240, 253–254.

When an adopted plan requires a qualifying close or stabilization, do not substitute an automatic buy at the quoted level. For an unfilled plan, raise or cancel the threshold only with a dated valuation, earnings, time-horizon or structural reason. Avoid chasing solely because the old entry was missed. Recalculate the remaining payoff after a gap, breakout or multi-day rally. For rolling positions, risk limits and re-entry, use the portfolio module.
