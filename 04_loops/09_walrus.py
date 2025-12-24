# value = 13
# remainder = value % 5

# if remainder :
#     print(f"Not divisible, remainder is {remainder}")


# Now using the walrus operator
value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")


available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter size: ")) in available_sizes:
    print(f"Serving {requested_size} size.")
else:
    print(f"Sorry, {requested_size} size is not available.")



# One More Example
flavours = ["masala", "ginger", "lemon", "mint"]

print("Available flavours: ", flavours)

while (flavour := input("Choose a flavour: ")) not in flavours:
    print("Sorry, we don't have that flavour. Please choose again.")

print(f"You choose {flavour} flavour.")