# Task 2: Internet Data Package Advisor

usage = float(input("Enter your data usage in GB: "))

if usage <= 5:
    package = "Basic Package"
elif usage <= 15:
    package = "Standard Package"
else:
    package = "Premium Package"

print(f"Recommended Package: {package}")