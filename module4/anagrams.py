def is_anagram_of(a, b):
    # make every words into lowercase
    a = a.lower()
    b = b.lower()
    
    # create a dictionary that holds how often a letter occurs in a
    dic_a = {}
    for i in a:
        if i != ' ' and i not in dic_a:
            dic_a[i] = 1
        elif i != ' ' and i in dic_a:
            dic_a[i] += 1
    
    # see how often a letter occurs in b and give a minus point in dictionary
    for i in b:
        if i != ' ' and i in dic_a:
            dic_a[i] -= 1
        if i != ' ' and i not in dic_a:
            dic_a[i] = -1
    print(dic_a.values())        

    # if a negative number appears in the value, give a minus point
    # otherwise, continue
    point = 0
    for i in dic_a.values():
        if i < 0:
            point -= 1
            
    if point == 0:
        return True
    else:
        return False

# is_anagram_of("eleven plus two", "twelve plus one")
# print(is_anagram_of("eleven plus two", "twelve plus one")) #True
# # e:3, l:2, v:1, n:1, p:1, u:1, s:1, t:1, w:1, o:1
# is_anagram_of("cat","tact")
# print(is_anagram_of("cat","tact")) #False
