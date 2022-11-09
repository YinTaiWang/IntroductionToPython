price = input("Enter the price of an article inculding VAT")
VAT = 21 / 100
# price = price * 1.21
price_without_vat = format(float(price) / (1 + VAT), '.2f')
print(f"This article will cost {price_without_vat} euro without {format(VAT*100, '.2f')}% VAT")