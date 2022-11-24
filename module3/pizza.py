def factorial(n):
    n_factorial = 1
    for i in range(1, n+1):
        n_factorial = n_factorial * i
    return n_factorial


def choose(n, k):
    numerator = factorial(n)
    k_factorial = 1
    nk_factorial = 1
    for i in range(1, k+1):
        k_factorial = k_factorial * i
    for j in range(1, n-k+1):
        nk_factorial = nk_factorial * j
    c_result = int(numerator/ (k_factorial * nk_factorial))
    return c_result
        

if __name__ == '__main__':
    mario = choose(10, 3)
    luigi = choose(9, 4)
    # print(mario)
    # print(luigi)
    if mario > luigi:
        winner = "Mario"
    else:
        winner = "Luigi"
        
    print(f"Mario can make {mario} pizzas.")
    print(f"Luigi can make {luigi} pizzas.")
    print(f"{winner} has won the bet.")  
    
