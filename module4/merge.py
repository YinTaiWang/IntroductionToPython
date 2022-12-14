def merge_sorted(a,b):
    largest_num = 0
    # Get the biggest number between a and b list
    if a[-1] > b[-1]:
        largest_num = a[-1]
    else:
        largest_num = b[-1]
    # print(largest_num)
    
    # make a dictionary to count how many times each number appears in both list
    count = {}
    for i in range(0, len(a)):
        if a[i] not in count:
            count[a[i]] = 1
        else:
            count[a[i]] += 1
    for i in range(0, len(b)):
        if b[i] not in count:
            count[b[i]] = 1
        else:
            count[b[i]] += 1
    # print(count)
    
    # loop over the numbers from 0, if it's in the dictionary
    # append the number(key) into c list x(value) times
    c = []
    for i in range(0, largest_num+1):
        if i in count.keys():
            j = count[i]
            # print(i, j)
            while j > 0:
                c.append(i)
                j -= 1
        else:
            continue
    # print(c)
    return c

# test
# a = [1, 2, 5, 8, 10]
# b = [2, 2, 6, 8, 9]
# merge_sorted(a,b)