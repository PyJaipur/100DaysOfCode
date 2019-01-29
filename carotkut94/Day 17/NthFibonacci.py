"""
A problem in which we have to find out the nth fibonacci number
"""


"""
In order to solve it the naive approach is to generate all the fibonacci upto given and return it
"""


def getFibOnN(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getFibOnN(n-1)+getFibOnN(n-2)


print(getFibOnN(10))



"""
Another approach is to memorize all the fibonacci numbers
"""


def getByMemorization(n, memorize = {1:0, 2:1}):
    if n in memorize:
        return memorize[n]
    else:
        memorize[n] = getByMemorization(n-1, memorize)+getByMemorization(n-2, memorize)
        return memorize[n]


print(getByMemorization(10))


""""
Using counter and list to store the next and previous fib number, without recursion
"""


def getCountedFibonacci(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0]+lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]


print(getCountedFibonacci(10))
