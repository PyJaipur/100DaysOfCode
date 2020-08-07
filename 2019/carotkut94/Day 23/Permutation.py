"""


Author Sidhant Rajora
"""


def getPermutation(array):
    perm = []
    permHelper(array, [], perm)
    return perm


def permHelper(array, current, perm):
    if not len(array) and len(current):
        perm.append(current)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPerm = current + [array[i]]
            permHelper(newArray, newPerm, perm)


print(getPermutation([1, 2, 3]))
