# Task 1: Daily Expense Tracker

food = 600
transport = 300
stationery = 200

total_expense = food + transport + stationery
budget = 1500

print("Daily Expense Tracker")
print("---------------------")
print(f"Food: {food} PKR")
print(f"Transport: {transport} PKR")
print(f"Stationery: {stationery} PKR")
print(f"Total Expense: {total_expense} PKR")
print(f"Daily Budget: {budget} PKR")

if total_expense > budget:
    print("Status: Budget exceeded.")
else:
    print("Status: Within budget.")