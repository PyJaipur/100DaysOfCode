# Solution statement for the problem statement of Day 1.
# Source Project Euler : https://projecteuler.net/problem=1

# Author : DeathCode94 aka carotkut94

# A holder variable for holding the upper limit for getting the sum of multiple of 3 or 5
# Simple solution involves a naive approach and involves a new list that consist the multiples and that list will have
# duplicate numbers like 15, 45 etx, then we can construct a set with those values and then we can call the sum method

UPPER_LIMIT = 1000
listOfNumbers = []
for i in range(0, UPPER_LIMIT, 3):
    listOfNumbers.append(i)

for i in range(0, UPPER_LIMIT, 5):
    listOfNumbers.append(i)

print(sum(set(listOfNumbers)))

# Using not in python
tempSum = 0
for i in range(UPPER_LIMIT):
    if not (i % 3 and i % 5):
        tempSum += i
print(tempSum)

# Single line solution for the problem statement using list comprehension
print(sum(i for i in range(UPPER_LIMIT) if not (i % 3 and i % 5)))


# All of the above methods returns the same output.
