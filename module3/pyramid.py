def alphabets(x):
    # unicode of alphabets
    a = ord('a')
    unicode_letter = ord(x)
    # three parts of the line
    a_to_y = ''
    z = ''
    y_to_a = ''
    lines = ''
    # the spaces, default width = 80
    front_space = 0
    for i in range(a, unicode_letter):
        a_to_y += chr(i)
        z = chr(unicode_letter)
        y_to_a += chr(a+unicode_letter-1-i)
        lines = a_to_y + z + y_to_a
        front_space = len(a_to_y)
    return front_space, lines

def pyramid(x):
    a = ord('a')
    unicode_letter = ord(x)
    rows = unicode_letter - a + 1
    range_w = range(a, unicode_letter+1)
    # print(range_w)
    for i in range(0, rows):
        spaces, words = alphabets(chr(range_w[i]))
        if i == 0:
            print((39-spaces) * ' ' + 'a' + (40-spaces) * ' ')
        else:
            print((39-spaces) * ' ' + words + (40-spaces) * ' ')
x = input()
pyramid(x)