def alphabets(x, y, z):
    string = ''
    for n in range(x, y, z):
        alphabet = chr(n)
        string += alphabet
    return string

letter = input()
a = ord('a')
unicode_letter = ord(letter)
a_to_y = alphabets(a, unicode_letter, 1)
z_to_a = alphabets(unicode_letter, a-1, -1)
print(a_to_y + z_to_a)

    