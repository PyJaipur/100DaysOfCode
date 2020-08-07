# Solution statement for the problem statement of Day 5.
# Source HackerRank : https://www.hackerrank.com/challenges/2d-array
# Statement : https://www.hackerrank.com/challenges/2d-array


# Solution

import os

rows = 6
columns = 6


def hourglass_sum(arr):
    max_sum = -9 * 9
    for i in range(rows - 2):
        for j in range(columns - 2):
            sum = (arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            max_sum = max(max_sum, sum)

    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
