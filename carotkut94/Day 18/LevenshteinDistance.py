"""
A problem that typically stats about transformation of a given string into another string by making edit operations
like insert, remove and substitution of a character.

We need to find out those minimum number of operations

Author Sidhant Rajora
"""


def lDistance(sample, target):

    countOfChanges = [[x for x in range(len(sample)+1)] for y in range(len(target)+1)]
    print(countOfChanges)
    for i in range(1, len(target)+1):
        countOfChanges[i][0] = countOfChanges[i-1][0] + 1
    for i in range(1, len(target)+1):
        for j in range(1, len(sample)+1):
            if target[i-1] == sample[j-1]:
                countOfChanges[i][j] = countOfChanges[i-1][j-1]
            else:
                countOfChanges[i][j] = 1 + min(countOfChanges[i-1][j-1], countOfChanges[i-1][j], countOfChanges[i][j-1])
    print(countOfChanges)
    # Select the last array from list and select the last element of that array
    return countOfChanges[-1][-1]


print(lDistance("abc", "yabd"))


"""
After taking look on the more optimized solution(slightly)
"""


def OlDistance(sample, target):
    small = sample if len(sample)<len(target) else target
    big = sample if len(sample) >= len(target) else target
    evenEdits = [x for x in range(len(small)+1)]
    oddEdits = [None for x in range(len(small)+1)]
    for i in range(1, len(big)+1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i
        for j in range(1, len(small)+1):
            if big[i-1] == small[j-1]:
                currentEdits[j] = previousEdits[j-1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j-1], previousEdits[j], currentEdits[j-1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]


print(OlDistance("abc", "yabd"))