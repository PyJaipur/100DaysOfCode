"""
A function for returning the sorted array of largest three numbers out of the given array

Author Sidhant Rajora
"""

def find(array):
    three = [None, None, None]
    for num in array:
        update(three, num)
    return three


def update(three, num):
    if three[2] is None or num > three[2]:
        shift(three, num, 2)
    elif three[1] is None or num > three[1]:
        shift(three, num, 1)
    elif three[0] is None or num > three[0]:
        shift(three, num, 0)


def shift(array, num, index):
    for i in range(index+1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i+1]


print(find([1, 6, 3, 6, 90, 2, 4, 68, 354, 235, 4, 567]))
