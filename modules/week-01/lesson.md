# Lesson: Financial records to investigative leads

Financial investigation data science combines evidence evaluation with reproducible computation. Fraud generally involves deception for gain; money laundering concerns criminal proceeds and applicable law. AML = anti-money laundering; KYC = know your customer; CDD = customer due diligence; SAR = suspicious activity report. This course is simulated internal analysis, not real reporting.

A transaction has a unique ID, timestamp, sender, receiver, amount and channel. Each row represents one transfer. Count it once for total volume. Net flow is receipts minus payments, not an ending balance without complete history and opening balances.

Example: a $7,000 payment to a new vendor is an observation. Inconsistent activity is a hypothesis; an equipment purchase is an alternative explanation. An invoice might corroborate it. No single amount establishes wrongdoing. Keep raw records unchanged, record assumptions, cite transaction IDs and distinguish facts from inferences.

## Python basics
A variable is a named value. Strings hold text, integers whole numbers, Booleans True or False. A comparison such as amount >= 5000 returns a Boolean. An if statement runs its indented block when the condition is true. Lists store items; dictionaries associate keys with values; for loops process items one by one. print displays output, len counts items, sum adds numbers and max selects the largest.

CSV stores tabular text. csv.DictReader gives each row as a dictionary of strings. Convert amount_usd to int before arithmetic. The training data use whole USD amounts; real financial applications should use exact monetary arithmetic (integer minor units or Decimal), defined currency conversions and validation.

A screening threshold is an analyst-defined rule here, not a legal reporting threshold. An alert is a lead; review context, alternative explanations and limitations. Never publish real customer information or credentials.
