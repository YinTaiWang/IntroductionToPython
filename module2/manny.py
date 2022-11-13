money = 0
while True:
    if money < 50:
        money = float(input("Enter the amount you want to donate: \n"))
    else:
        print(f"Thank you very much for your contribution of {format(money, '.2f')} euro.")
        break