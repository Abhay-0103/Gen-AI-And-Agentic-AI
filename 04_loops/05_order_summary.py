names = ["Abhay", "Lucky", "Zoro", "Sanji"]

bills = [250, 300, 150, 400, 350]

for name, amount in zip(names, bills):
    print(f"Customer: {name} Toatl Bill Amount: ${amount}")