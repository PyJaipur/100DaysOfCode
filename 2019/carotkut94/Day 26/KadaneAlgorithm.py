"""
Implementation of kadane's algorithm
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

Author Sidhant Rajora
"""


def kadaneAlgo(array):
    maxEnding = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        num = array[i]
        maxEnding = max(num, maxEnding + num)
        maxSoFar = max(maxSoFar, maxEnding)
    return maxSoFar


print(kadaneAlgo([1, 2, 3, -3, -1, 4, 5, -1, 6]))
