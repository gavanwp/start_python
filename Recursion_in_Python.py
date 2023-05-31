# Recursion in Python 


# factorail(5) = 5*4*3*2*1 
# factorial(4) = 4*3*2*1 
# factorial(0) = 1

def add(a):
    if (a == 0 or a == 1):
        return a
    else:
        return a + add(a-1)


print(add(10))


# Fibonacci  saquence 

# f(0) = 0 
# f(1) = 1 
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-0)

# 0 1 1 2 3 5 8 13