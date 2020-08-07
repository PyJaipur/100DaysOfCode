"""
Absolute minimum difference with one removal operation on entire array

Author Sidhant Rajora
"""

def minimumSumArrat(A):
    minimum = max(A)
    for i in A:
        sumofminimum = 0
        tempList = A.copy()
        tempList.remove(i)
        for i in range(1, len(tempList)):
            sumofminimum += abs(tempList[i-1]-tempList[i])
        if sumofminimum <= minimum:
            minimum = sumofminimum
    return minimum


print(minimumSumArrat([1, 5, 3, 2, 10]))
