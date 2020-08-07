"""
You are given a non-empty array of integers. Each element represents the maximum number of steps you can take forward.
For example, if the element at index 1 is 3, you can go from index 1 to index 2, 3, or 4.
Write a function that returns the minimum number of jumps needed to reach the final index. Note that jumping from
index i to index i + x always constitutes 1 jump, no matter how large x is.

Author Sidhant Rajora
"""


def minJumps(array):
    if len(array) == 1:
        return 0
    jumps = 0
    reach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        reach = max(reach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = reach - i
    return jumps + 1


print(minJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
