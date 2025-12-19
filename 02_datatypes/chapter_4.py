# Boolean Upcasting

is_boiling = True  # 1
stri_count = 5
total_actions = stri_count + is_boiling   # Upcasting
print(f"Total actions: {total_actions}")


milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")  # Upcasting


# Logical Operations and, or, not
water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}") # Downcasting