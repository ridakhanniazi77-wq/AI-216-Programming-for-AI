# Task 4: Loan Eligibility Simulation

incomes = [75000, 45000, 80000, 55000, 65000]
employment_status = ["Employed", "Employed", "Employed", "Unemployed", "Employed"]

eligible_count = 0

for i in range(len(incomes)):
    if incomes[i] >= 60000 and employment_status[i] == "Employed":
        eligible_count += 1

print("Loan Eligibility Simulation")
print("----------------------------")
print(f"Total applicants: {len(incomes)}")
print(f"Eligible applicants: {eligible_count}")