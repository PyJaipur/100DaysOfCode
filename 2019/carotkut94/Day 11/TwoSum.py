# Problem from AlgoExpert (can be found at LeetCode as well)
# Name : TwoSum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Author : Sidhant Rajora


# Solution 1
# Using for loop two times to iterate over

def twoNumberSumFor(array, target):
    for i in range(len(array) - 1):
        num = array[i]
        for j in range(i+1, len(array)):
            num2 = array[j]
            if num+num2 == target:
                return sorted([num, num2])
    return []


print(twoNumberSumFor([3, 5, -4, 8, 11, 1, -1, 6], 10))

# Solution 2
# Using HashMap or Dictionary


def twoNumberSum(array, targetSum):
    table = {}
    for i in array:
        if targetSum - i in table:
            return sorted([targetSum-i, i])
        else:
            table[i] = True
    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
