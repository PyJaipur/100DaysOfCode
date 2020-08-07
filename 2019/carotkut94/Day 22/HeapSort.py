"""
Standard heap sort implementation, more about heap sort can be found at : https://en.wikipedia.org/wiki/Heapsort


Author Sidhant Rajora
"""


def heap_sort(array):
    buildMaxHeap(array)
    for end in reversed(range(1, len(array))):
        swap(0, end, array)
        shiftDown(0, end - 1, array)
    return array


def buildMaxHeap(array):
    firstParent = (len(array) - 2) // 2
    for i in reversed(range(firstParent+1)):
        shiftDown(i, len(array)-1, array)


def shiftDown(current, end, heap):
    child = current * 2 + 1
    while child <= end:
        child2 = current * 2 + 2 if current * 2 + 2 <= end else -1
        if child2 > -1 and heap[child2] > heap[child]:
            swapIndex = child2
        else:
            swapIndex = child
        if heap[swapIndex] > heap[current]:
            swap(current, swapIndex, heap)
            current = swapIndex
            child = current * 2 +1
        else:
            return


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(heap_sort([8, 7, 4, 2]))
