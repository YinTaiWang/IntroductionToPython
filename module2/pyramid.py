width = int(input("Please enter the pyramid width \n"))

def asterisk(width):
    for i in range(1, width+1, 2):
        space = int((width - i) / 2)
        print(space * " " + i  * "*")
    
while True:
    if width % 2 == 0:
        print("Please enter an odd number")
        width = int(input("Please enter the pyramid width \n"))
    else:
        asterisk(width)
        break