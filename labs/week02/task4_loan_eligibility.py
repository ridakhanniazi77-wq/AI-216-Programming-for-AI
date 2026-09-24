incomes = [65000, 45000, 80000, 55000, 70000]
employment_status = ["Employed", "Employed", "Employed", "Unemployed", "Employed"]

eligible_count = 0

for income, status in zip(incomes, employment_status):
    if income >= 60000 and status == "Employed":
        eligible_count += 1

print("Eligible applicants:", eligible_count)