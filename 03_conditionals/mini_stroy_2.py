# Snack Suggestion System
# This program suggests a snack based on the user's preferences.

snack = input("Enter your preferred snack: ").lower()
print(f"User said: {snack}")

if snack == "cookies" or snack == "cake":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print(f"Sorry, we don't have {snack}. please choose other snacks.")