# Solution statement for the problem statement of Day 7.
# Source Wikipedia : https://en.wikipedia.org/wiki/Merge_sort
# Statement : Merge Sort implementation


# Implementation


def merge_lists(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        m = int(len(input_list) / 2)
        l = merge_sort(input_list[:m])
        r = merge_sort(input_list[m:])
        return merge_lists(l, r)


number_list = [3, 1, 5, 10, 3, 4, 2, 9, 8, 11, 34, 26, 72, 13, 151, 16]
print(merge_sort(number_list))


# I read an academic paper on modified merge sort, once i get hold of that paper and algorithm
# I will implement that too and will see how does both of those work on last data set
