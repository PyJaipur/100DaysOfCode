"""

find out all subarray containing four numbers such that their sum is equal to target sum

Author Sidhant Rajora
"""


def fourSum(array, target):
    allPair = {}
    four = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            diff = target - currentSum;
            if diff in allPair:
                for pair in allPair[diff]:
                    four.append(pair + [array[i], array[j]])
        for k in range(0, 1):
            currentSum = array[i] + array[k]
            if currentSum not in allPair:
                allPair[currentSum] = [[array[k], array[i]]]
            else:
                allPair[currentSum].append([array[k], array[i]])
    return four


print(fourSum([7, 6, 4, -1, 1, 2], 16))
