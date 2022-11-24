def alphabets(x, y, z):
    string = ''
    for n in range(x, y, z):
        alphabet = chr(n)
        string += alphabet
    return string

a = ord('a')
z = ord('z')
a_to_y = alphabets(a, z, 1)
z_to_a = alphabets(z, a-1, -1)
print(a_to_y + z_to_a)

