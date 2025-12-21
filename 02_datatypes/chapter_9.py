# Sets 

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# Difference
only_in_essential = essential_spices - optional_spices
print(f"Spices only in essential: {only_in_essential}")

only_in_optional = optional_spices - essential_spices
print(f"Spices only in optional: {only_in_optional}")

# membership testing (case sensitive)
print(f"IS 'cloves' in essential spices ? {'cloves' in essential_spices}")

print(f"IS 'cloves' in optional spices ? {'cloves' in optional_spices}")