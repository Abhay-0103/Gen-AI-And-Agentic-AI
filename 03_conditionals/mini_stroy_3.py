# Mini Coffee Shop Program

cup_size = input("Choose Your Cup size (small/medium/large): ").lower()
print(f"You have chosen a {cup_size} cup.")

"""
if cup_size == "small": 
    print(f"It Cost 10rs.")
else:
    if cup_size == "medium":
        print(f"It Cost 20rs.")
    else:
        if cup_size == "large":
            print(f"It Cost 30rs.")
        else:
            print("Invalid cup size selected.")
"""
# New Method using elif

if cup_size == "small":
    print(f"It Cost 10rs.")
elif cup_size == "medium":
    print(f"It Cost 20rs.")
elif cup_size == "large":
    print(f"It Cost 30rs.")
else:
    print("Invalid cup size selected.")