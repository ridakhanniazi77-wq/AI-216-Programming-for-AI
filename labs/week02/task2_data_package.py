usage = float(input("Enter data usage in GB: "))

if usage <= 5:
    package = "Basic Package"
elif usage <= 15:
    package = "Standard Package"
else:
    package = "Premium Package"

print("Recommended:", package)