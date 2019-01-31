"""
We will implement the binary search in a rotated or shifted array algorithm read more about it at

Author Sidhant Rajora
"""

def shitedSearch(array, target):
    return doSearch(array, target, 0, len(array)-1)


def doSearch(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    match = array[mid]
    leftNum = array[start]
    rightNum = array[end]
    if target == match:
        return mid
    elif leftNum <= match:
        if match > target >= leftNum:
            return doSearch(array, target, start, mid)
        else:
            return doSearch(array, target, mid + 1, end)
    else:
        if match < target <= rightNum:
            return doSearch(array, target, mid + 1, end)
        else:
            return doSearch(array, target, start, mid - 1)


print(shitedSearch([3, 4, 1, 2], 1))
