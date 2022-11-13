price_1 = float(input("Enter the price of the first article: "))
price_2 = float(input("Enter the price of the second article: "))
price_3 = float(input("Enter the price of the third article: "))
all_products = [price_1, price_2, price_3]
# print(all_products)
discount = 0.15
max = 0
for i in range(0, len(all_products)):
    if all_products[i] > max:
        max = all_products[i]
discount_price = max * discount
total = sum(all_products) - discount_price
print(f"Discount: {format(discount_price, '.2f')}")
print(f"Total: {format(total, '.2f')}")
