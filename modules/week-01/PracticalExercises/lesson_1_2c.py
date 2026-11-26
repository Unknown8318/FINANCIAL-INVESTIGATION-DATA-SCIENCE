transactions = [1200, 300, 5000, 200, 7300]

counter = 0

for amount in transactions:
    counter += 1
    print("Iteration:", counter, "Amount:", amount)

print("Total iterations:", counter)