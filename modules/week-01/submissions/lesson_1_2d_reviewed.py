# Import required modules
import csv
from pathlib import Path

# Locate the financial transaction file
file_path = Path(__file__).parent.parent / "data" / "practice_transactions.csv"

# Verify the file location
print("File location:", file_path)
print("File exists:", file_path.exists())

# Open and read the CSV file
with file_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    transactions = list(reader)

# Display imported information
print("Total records:", len(transactions))
print("First transaction:", transactions[0])

# Counters and Storing Values for future for loops and transactions amounts
flagged_counter = 0
flagged_amount = 0
flagged_id = []

total_counter = 0
total_tansaction = 0

review_threshold = 5000

#looping through the table to review to and from data, along with transaction amount. 
# simultaneiously looking through a review threshold
for transaction in transactions:
    total_counter +=1
    total_tansaction += int(transaction["amount_usd"])
    if int(transaction["amount_usd"]) >= review_threshold:
        print("dest: ", transaction["destination_account"], 
            ", source: ", transaction["source_account"], 
            ", transaction amount: ", transaction["amount_usd"])
        
        flagged_counter+=1
        flagged_amount += int(transaction["amount_usd"])
        flagged_id.append(transaction["transaction_id"])

flagged_percentage = float((flagged_counter/total_counter) * 100)
flagged_amount_percentage = float((flagged_amount / total_tansaction)*100)

print("\n---- Flagged Transactions for Review ----")
print(f"Total Flagged Transactions: {flagged_counter} |  Total Flagged Transferred:  ${flagged_amount:.2f}")
print(f"Transaction IDs requiring further review: {flagged_id}")
print(f"Percentage of flagged transactions: {flagged_percentage}%")
print(f"Percentage of flagged amounts: {flagged_amount_percentage:.2f}%")

print(" \n---- Total Transactions and Amount Transferred ----")
print(f"Total  Transactions: {total_counter} |  Total  Transferred:  ${total_tansaction:.2f}")
