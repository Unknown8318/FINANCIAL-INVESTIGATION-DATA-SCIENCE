"""Guided tutorial: run, modify, and predict the results."""
import csv
from pathlib import Path

account = "P001"
amount = 1200
review_threshold = 5000  # Classroom rule, not law.
print(f"Account: {account}; amount: ${amount:,}")
if amount >= review_threshold:
    print("Amount screen: review")
else:
    print("Amount screen: not triggered")

path = Path(__file__).parent / "data" / "practice_transactions.csv"
with path.open(newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

total = 0
flagged = []
for row in rows:
    value = int(row["amount_usd"])
    total = total + value
    if value >= review_threshold:
        flagged.append(row["transaction_id"])

print(f"Transactions: {len(rows)}")
print(f"Total volume: ${total:,}")
print(f"Screened IDs: {flagged}")
# Expected: 5 rows, $14,000, P003 and P005.
