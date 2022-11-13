number = []
int_number = []
numbers = str(input("Please enter some numbers: "))
number = numbers.split(" ")
for i in number:
    i = int(i)
    int_number.append(i)
int_number.sort()
print(int_number[1])