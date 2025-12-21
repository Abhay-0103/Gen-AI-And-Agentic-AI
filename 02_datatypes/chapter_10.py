# Dictionary

chai_order = dict(type="Masala Chai", size="Large", sugar = 2 )
print(f"Chai Order: {chai_order}")

# In-Depth Dictionary Operations
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "water and milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe before Deletion: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe after Deletion: {chai_recipe}")

# Membership Test
print(f"Is sugar in the order ? {'sugar' in chai_order}")

# New Order
chai_order = dict(type="Ginger Chai", size="Medium", sugar = 1 )
print(f"New Chai Order: {chai_order}")

# Prining only Keys
print(f"Order details (keys): {chai_order.keys()}")

# Prining only Values
print(f"Order details (values): {chai_order.values()}")

# Printing Items
print(f"Order details (items): {chai_order.items()}")

# Removing Last Item
last_item = chai_order.popitem()
print(f"Last item removed: {last_item}")

# Updating Dictionary
extra_spices = {"cardamom" : "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated Spices: {chai_recipe}")

# Size of Dictionary
chai_size = chai_order["size"]
print(f"Updated Chai Size: {chai_size}")

# Better to use get() to avoid KeyError
customer_note = chai_order.get("note", "No Instructions Found")
print(f"Customer Note: {customer_note}")