sequence = []
start = int(input("Please enter a number: "))
sequence.append(start)

i = 0
while sequence[i] != 1:
    if sequence[i] % 2 == 0:
        sequence.append(int(sequence[i]/2))
        i += 1 
    else:
        sequence.append(int(3 * sequence[i] + 1))
        i += 1

M = len(sequence)
for i in range(M):
    sequence[i] = str(sequence[i])
output = ' '.join(sequence)
print(output)
