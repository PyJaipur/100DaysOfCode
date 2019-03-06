"""
Given an array arr[] of integers, find out the maximum
difference between any two
elements such that larger element appears after the smaller number.
"""

"""
this is a naive approach that runs in O(n^2)
"""


def maxDiff(arr):
    max_diff = arr[1] - arr[0]

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > max_diff:
                print(arr[j])
                print(arr[i])
                print(max_diff)
                max_diff = arr[j] - arr[i]
                print(max_diff)
                print("=============index==============")
                print(i)
                print(j)
                print('++++++++++++++++++++++++++++')
    return max_diff


#print(maxDiff([2, 3, 10, 6, 4, 8, 1]))

"""
Efficient approach over the proposed solution above
"""
def effDiffMax(arr, l):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]

    for i in range(1, l):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element

        if arr[i] < min_element:
            min_element = arr[i]
    return max_diff


print(effDiffMax([1, 2, 6, 80, 100], 5))
