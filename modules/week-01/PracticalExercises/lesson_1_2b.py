transactions = [
    {"id": "P001", "amount": 1200},
    {"id": "P002", "amount": 300},
    {"id": "P003", "amount": 5000},
    {"id": "P004", "amount": 200},
    {"id": "P005", "amount": 7300}
]

flagged_count = 0
flagged_total = 0

for all in transactions:
    print("Account ID: ", all["id"], ", transaction amount: ", all["amount"])

for transaction in transactions:
    if transaction["amount"] >= 5000:
        print(transaction["id"], transaction["amount"])
        flagged_count +=1
        flagged_total = flagged_total + transaction["amount"]

print(flagged_count)
print(flagged_total)
print(transactions[0]["amount"])