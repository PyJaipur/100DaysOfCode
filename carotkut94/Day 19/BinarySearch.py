"""
We will implement the standard binary search algorithm read more about it at
https://en.wikipedia.org/wiki/Binary_search_algorithm
Author Sidhant Rajora
"""



def binarySearch(array, target):
    return doSearch(array, target, 0, len(array)-1)


def doSearch(array, target, start, end):
    while start < end:
        mid = (start+end) // 2
        matchable = array[mid]
        if target == matchable:
            return mid
        elif target < matchable:
            end = mid - 1
        else:
            start = mid + 1


print(binarySearch([1, 4, 5, 6, 7, 8, 9], 8))
