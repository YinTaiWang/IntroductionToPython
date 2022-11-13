sequence = []
start = int(input("Please enter a number: "))
sequence.append(start)
for i in range(0, 100000):
    if sequence[i] % 2 == 0:
        sequence.append(int(sequence[i]/2))
    elif sequence[i] == int(1):
        break
    else:
        sequence.append(int(3 * sequence[i] + 1))
M = len(sequence)
for i in range(M):
    sequence[i] = str(sequence[i])
output = ' '.join(sequence)
print(output)
