numbers = input("Please enter some numbers: ")
number = numbers.split(" ")
number = list(map(int, number))

M = len(number)
for t in range(0, M):
    for i in range(0, M-1):
        if number[i] > number[i + 1]:
            number[i], number[i + 1] = number[i + 1], number[i]
print(number)
