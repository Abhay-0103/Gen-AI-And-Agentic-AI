flavours = ["vanilla", "chocolate", "strawberry", "mint", "cookie dough"]

for flavour in flavours:
    if flavour == "strawberry":
        continue
    if flavour == "chocolate":
        break
    print("chocolate is the best flavour")

print("Out side the loop")