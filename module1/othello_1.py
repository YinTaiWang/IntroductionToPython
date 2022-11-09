white = int(input("Enter the number of white pieces on the board:"))
black = int(input("Enter the number of black pieces on the board:"))
total_squares = 64
percentage_black = (black / (white + black)) * 100
percentage_of_all_black = (black / total_squares) *100
print(f"The percentage of black pieces on the board is: {format(percentage_of_all_black, '.2f')}%")
print(f"The percentage of black pieces of all the pieces on the board is: {format(percentage_black, '.2f')}%")