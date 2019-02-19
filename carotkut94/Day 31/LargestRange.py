"""
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of
numbers contained in that array. The first number in the output array should be the first number in the range while the
second number should be the last number in the range. A range of numbers is defined as a set of numbers that come right
after each other in the set of real integers. For instance, the output array [2, 6] represents the range
{2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers do not need to be ordered or adjacent in the array in
order to form a range. Assume that there will only be one largest range.


Author Sidhant Rajora
"""


def largestRange(array):
    best = []
    longest = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        current = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            current += 1
            left -= 1
        while right in nums:
            nums[right] = False
            current += 1
            right += 1
        if current > longest:
            longest = current
            best = [left+1, right-1]
    return best


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))