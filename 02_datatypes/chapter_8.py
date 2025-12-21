# List 

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are : {ingredients}")
ingredients.remove("water")
print(f"Ingredients are : {ingredients}")

# Extending and Inserting in Lists
spice_options = ["Ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

# Extend chai_ingredients with spice_options
chai_ingredients.extend(spice_options)

# Insert "black tea" at index 2
chai_ingredients.insert(2, "black tea")
print(f"Chai Ingredients are : {chai_ingredients}")

# pop the last added ingredient
last_added = chai_ingredients.pop()
print(f"{last_added} was the last added ingredient.")
print(f"Chai Ingredients are : {chai_ingredients}")

# Reversing and Sorting Lists
chai_ingredients.reverse()
print(f"Reversed Chai Ingredients are : {chai_ingredients}")

chai_ingredients.sort()
print(f"Sorted Chai Ingredients are : {chai_ingredients}")

# Variables and Identity
sugar_level = [1,2,3,4,5]
print(f"Maximum sugar level is {max(sugar_level)}")
print(f"Minimum sugar level is {min(sugar_level)}")

# Operator Overloading
base_liquids = ["water", "milk"]
extra_flavors = ["ginger"]

full_liquids_mix = base_liquids + extra_flavors
print(f"Full liquids mix: {full_liquids_mix}")

# Array in Operations Overloading
strong_brew = ["black tea", "water"] * 3
print(f"Strong brew mix: {strong_brew}")

# String Covtering into list
raw_spice_data = bytearray(b"Cinnamon")
raw_spice_data = raw_spice_data.replace(b"Cinna", b"Card")
print(f"Raw spice data as list: {raw_spice_data}")