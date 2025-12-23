staff = [("Abhay", 21), ("John", 15), ("Sara", 10)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is an adult.")
        break
else:
    print("No adults found in the staff list.")