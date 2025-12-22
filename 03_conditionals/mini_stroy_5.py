# wavier 

order_amount = int(input("Enter the order amount: "))
# print(f"Order amount: {type(order_amount)}")

delivery_fees = 0 if order_amount > 300 else 50
print(f"Delivery fees: {delivery_fees}")

total_amount = order_amount + delivery_fees
print(f"Total amount: {total_amount}") 