# Source interpretation and refresh discipline

## What the correction files establish

The 2026-09-26 inventory contains 255 transcript text files and three auxiliary files: `README-corrections.md`, `RhinoFinance-vocabulary.txt`, and `correction-review-notes.md`. The README describes a 2026-09-23 context-based correction pass. It explicitly disclaims audio verification and a factual audit. Its correction counts are that document's claims, not independent validation performed by this skill.

The vocabulary contains prompt terms and exact `source => replacement` pairs. Use it to understand recurring terminology such as 前瞻估值, 未平仓, 轧空 and 止跌形态. Do not apply all replacements blindly to new material. In particular, ISI, Cloud, SRG, CIM and MTU can be valid names or securities. Resolve entities from the surrounding discussion and verify the exchange/ticker for current research. A malformed price, unit or date must stay unresolved until grounded; never repair it by intuition.

The README names four additional JSON resources (`whisper-replacements.json`, `whisper-context-review.json`, `whisper-vocabulary-evidence.json`, `correction-manifest.json`) that were not present in this folder inventory. Do not claim to have inspected them. The three available auxiliary files and inline notes provide the available correction provenance.

## Preserve uncertainty

- Keep filename date, header date, literal spoken session date and Drive modification time separate. The upload time is not the event date. A one-day timezone difference may be normal; conflicting year/day/date text needs verification. Do not silently normalize inconsistencies.
- Check numerical units and context: percentage versus percentage points/basis points, per-share earnings versus currency millions/billions, capex growth versus spending level, EPS fiscal year versus calendar year. Missing chart context can make an apparently precise range unusable.
- Treat “support,” “fair value,” “cost,” “target” and “upper/lower bound” as different concepts. A reversed or inconsistent interval in a source is not an executable signal.
- Verify institutional attribution, source date and coverage before using survey percentages, CTA triggers, short interest or options positioning. Preserve explicit unavailable-data admissions. An inferred estimate is not a fresh provider update.
- Do not infer the direction of all investor flows from one chart, claim every fund profits from volatility, equate oversold with safe, or reproduce unsupported causal statements merely because they recur in the corpus.
- Do not convert the presenter's conviction into empirical accuracy. Neither a 33% winners/losers heuristic nor historical rebound examples supply calibrated current probabilities.

Use the catalog's `review_notes` for specific transcript ambiguities and use its public video reference or an authorized source-file copy for exact context. Private Google Drive links and IDs are omitted from this public export. The collection supplies analytical patterns; it does not verify the reported events, investment outcomes, proprietary models or original audio.

## Refresh the collection

1. Obtain the source folder from the user or their authorized connected files; this public export does not include its private location. Enumerate all current direct children and any subfolders through the available Drive tools. Resolve shortcuts if present, follow pagination, and check result caps. Record unreadable files, duplicates and auxiliary files separately. Do not equate a search result cap with the folder total.
2. Retrieve complete readable content. Compare retrieved UTF-8 bytes with the reported size for stored text where equivalent; resolve truncation before treating a file as covered. Preserve hashes, names, URLs and modified timestamps.
3. Match the existing catalog by video URL or exact filename, then content hash, rather than Drive ID alone. A correction upload may replace every ID. Retain stable catalog indices so method references do not drift. Record newly added, revised and missing sources without treating a replacement as an additional independent observation.
4. Read correction documentation, scan every transcript for relevant methods, and examine source passages for each substantive new or changed rule. Review chronological sequences that include failures, cancellations and later revisions as well as favorable examples. State the review method honestly; complete retrieval and automated indexing are not a claim of an audio audit or sentence-by-sentence factual validation.
5. Update the method references and source map, retaining conditional reasoning rather than historical calls, personal limits or obsolete prices. Label any added implementation safeguards separately from the presenter's methods. Run skill validation and save the existing personal skill through the skill-creator workflow.

Do not reread the entire corpus for routine investment questions. Load the relevant method module and current primary evidence; retrieve individual transcripts only for attribution, a historical comparison or another corpus update.
