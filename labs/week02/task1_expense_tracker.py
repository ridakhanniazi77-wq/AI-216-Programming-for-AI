food = 700
transport = 300
stationery = 200

total_expense = food + transport + stationery
budget = 1500

print("Daily Expense Tracker")
print("Food:", food, "PKR")
print("Transport:", transport, "PKR")
print("Stationery:", stationery, "PKR")
print("Total Expense:", total_expense, "PKR")

if total_expense > budget:
    print("Budget exceeded.")
else:
    print("Within budget.")