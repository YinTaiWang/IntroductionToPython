words = []
a = ord('a')
z = ord('z')
for i in range(a, z+1):
    words.append(chr(i))
alphabet = ''.join(words)
print(alphabet)
