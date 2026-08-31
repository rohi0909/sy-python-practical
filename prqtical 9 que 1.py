# Consumer Transaction Tracking Program

transactions = []

# Accept five transaction values
for i in range(5):
    amount = float(input(f"Enter transaction {i + 1}: ₹"))
    transactions.append(amount)

# Find largest transaction
largest = max(transactions)

# Calculate average spending
average = sum(transactions) / len(transactions)

# Display results
print("\n--- Transaction Summary ---")
print("Transaction values:", transactions)
print(f"Largest transaction: ₹{largest:.2f}")
print(f"Average spending: ₹{average:.2f}")
