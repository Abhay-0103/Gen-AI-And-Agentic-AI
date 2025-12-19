# Strings

chai_type = "Ginger chai"
customer_name = "lucky"

print(f"Order for {customer_name} : {chai_type}")

# Indexing
chai_description = "Aromatic and bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}") # Reversing the string


label_text = "chai Special"
ecoded_label = label_text.encode("utf-8")
print(f"Encoded label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")