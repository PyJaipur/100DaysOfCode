# Solution statement for the problem statement of Day 4.
# Source HackerRank : https://www.hackerrank.com/challenges/ctci-array-left-rotation
# Statement : A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example,
# if 2 left rotations are performed on array [1,2,3,4,5] , then the array would become [3,4,5,1,2].
# Given an array a of n integers and a number,d, perform d left rotations on the array. Return the updated array
# to be printed as a single line of space-separated integers.


# Author : Deathcode aka carotkut94

# It is an easy problem and i just pasted the code i did on hackerrank, but modified it a little


def rotate_left(a, d):
    temp_result = a[d % len(a):len(a)]+a[0:d % len(a)]
    return temp_result


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    d = 2
    result = rotate_left(a, d)
    print(result)
