transactions = [
    {"id": "P001", "amount": 1200},
    {"id": "P002", "amount": 300},
    {"id": "P003", "amount": 5000},
    {"id": "P004", "amount": 200},
    {"id": "P005", "amount": 7300}
]

flagged_count = 0
flagged_total = 0

transactions = [1200, 300, 5000, 200, 7300]

print(f'Transaction Count = {len(transactions)}')
print(f'Total Volume: {sum(transactions)}')
print(f'Largest Transaction: {max(transactions)}')
print(f'Smallest Transaction: {min(transactions)}')

average_transaction = float(sum(transactions)/len(transactions))
print(f'Average Transaction: ${average_transaction:.2f}')
