# Solution statement for the problem statement of Day 8.
# Source Wikipedia : https://en.wikipedia.org/wiki/Quick_sort
# Statement : Quick Sort implementation


# Implementation

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        p1 = quicksort(x[:i])
        p2 = quicksort(x[i + 1:])
        p1.append(x[i])
        return p1 + p2


number_list = [3, 1, 5, 10, 3, 4, 2, 9, 8, 11, 34, 26, 72, 13, 151, 16]
print(quicksort(number_list))
