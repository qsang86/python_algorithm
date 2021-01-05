def factorial(n):

    #1! = 1 / 2! = 1*2 / 3! = 3*2*1
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n >= 2:
        return n*factorial(n-1)

    #n=4/ 4*fac3

print(factorial(5))