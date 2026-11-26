# Week 01 — Learning notes and code review
## Concepts covered
- 1.2A: variables, strings, integers, Booleans, assignment and comparisons.
- 1.2B: lists, zero-based indexes, dictionary keys, sum/len/max/min and mean. Remediation: dictionary access uses keys, not positions.
- 1.2C: for loops, indentation, counters and accumulators. Remediation: n records means n loop-body executions in a complete standard loop, last index n-1.
- 1.2D: pathlib, portable paths, csv.DictReader, list of dictionaries, int conversion, conditional screening, collecting IDs with append, and percentages.

## Reviewed submission
The learner's latest chat-submitted script is preserved in lesson_1_2d_reviewed.py. Run from repository root: python modules/week-01/submissions/lesson_1_2d_reviewed.py. Static review only; expected results for the practice dataset: 5 records, $14,000 total volume, 2 flagged records (P003 and P005), $12,300 flagged volume, 40% flag rate, 87.86% flagged volume. Screening is not evidence of wrongdoing.

Suggested improvements (not applied to learner's code): convert amount once per row; use descriptive names; format money with thousands separators; guard empty data and zero denominators; distinguish undefined percentages from zero.

## Optional nested dictionary extension
Initialize flagged_tx = {} before the loop. Inside the screening condition:
```python
flagged_tx[transaction["transaction_id"]] = {
    "source": transaction["source_account"],
    "destination": transaction["destination_account"],
    "amount": int(transaction["amount_usd"])
}
```
Dictionary assignment is not list append. Duplicate transaction IDs would overwrite earlier entries, so validate uniqueness before relying on this structure. Extension discussed, not yet assessed.

## Pending investigative assessment
1. Interpret the difference between flag count rate and flagged volume rate.
2. Describe the relationship between P001 and P003.
3. Identify plausible legitimate explanations.
4. Identify additional authorized records to request.
5. Assess whether evidence establishes fraud or money laundering, with reasoning.

CSV knowledge check remains pending. Next lesson: functions.
