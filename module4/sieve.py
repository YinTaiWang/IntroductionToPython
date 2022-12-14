def cross_out_multiples(is_prime,n) :
    for i in range(1, len(is_prime)):
        if i % n == 0:
            is_prime[i] = False
    return is_prime

# l = [True for i in range(0,20)]
# # print(l)
# print(cross_out_multiples(l, 3))
# cross_out_multiples(l, 3)

def sieve(n):
    # create a list from 0 to n
    all_num = []
    for i in range(0, n+1):
        all_num.append(i)
    # make a boolean list for all the numbers below n
    l = [True for i in range(0,n)]
    
    x = 2
    while (x*x) < n:
        # get boolean values that count if the number is a multiple of x
        l = cross_out_multiples(l, x)
        # print(l)
        # except the boolean value before x, loop over every value
        for i in range(x+1, len(l)):
            if l[i] == False:
                if i in all_num:
                    all_num.remove(i)
                else:
                    continue
        # print(l)
        x += 1
    
    # remove 0, 1, n from the list
    all_num.remove(0)
    all_num.remove(1)
    all_num.remove(n)
    return all_num

# test
# sieve(100)