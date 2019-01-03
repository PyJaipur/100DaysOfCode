# Solution statement for the problem statement of Day 2.
# Source Leetcode : https://leetcode.com/problems/single-number
# Statement : Given a non empty array of integers, every element is repeated twice except for one,
# find that single unique number
# Author : Deathcode aka carotkut94

# I started of with a mathematical approach to solve this problem
# Lets assume that we have an array [4,4,1,3,3,1,2]
# and the sum of the array is sum([4,4,1,3,3,1,2]) = 18
# and if I find the sum of unique elements of the array i.e sum([4,1,3,2]) = 10 and if I double this i.e 10*2 = 20
# and if I subtract the sum of all number from twic the sum of unique elements of the array we will get the unique
# number i.e 20-18 = 2 and we can see that 2 is our number.

a = [4, 4, 1, 3, 3, 1, 2]
sumOfAll = sum(a)
twiceUniqueSum = 2*(sum(set(a)))

print(twiceUniqueSum-sumOfAll)

# On the other i realized that this approach has its own flaws, it is mathematical in nature but requires more space
# Then after looking in it, i realized XOR operation can be done and it will return the unique number to me.

a = [4, 4, 1, 3, 3, 1, 2]
x = 0
for i in a:
    x ^= i
print(x)

# In this approach the time complexity will remain the same i.e O(n) but not extra space is used.
