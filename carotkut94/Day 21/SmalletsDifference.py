"""
In this problem we are given two non empty arrays and we need to find the pair such that first element from first array
and second element of the pair will be from the second array and the difference between pair element is closest
to zero(0)


Author Sidhant Rajora
"""


def smallDiff(array1, array2):
    array1.sort()
    array2.sort()
    index1 = 0
    index2 = 0
    smallest = float("inf")
    smallPair = []
    while index1 < len(array1) and index2 < len(array2):
        f = array1[index1]
        s = array2[index2]
        if f < s:
            current = s - f
            index1 += 1
        elif s < f:
            current = f - s
            index2 += 1
        else:
            return [f, s]
        if smallest > current:
            smallest = current
            smallPair = [f, s]
    return smallPair


print(smallDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
