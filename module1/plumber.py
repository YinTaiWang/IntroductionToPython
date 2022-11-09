wages = input("Enter the hourly wages:")
hours = float(input("Enter the number of hours worked:"))
rounded_hours = int(hours + 0.5)
callout_cost = 16.00
cost = float(wages) * rounded_hours + callout_cost
print(f"The total cost of this repair is: {format(cost, '.2f')} euro")
