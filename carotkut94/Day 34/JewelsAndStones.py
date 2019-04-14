"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

This problem can be found at : https://leetcode.com/problems/jewels-and-stones/

Author: Sidhant Rajora
"""


def numJewelsInStones(J: str, S: str) -> int:
    count = 0
    for c in J:
        count += S.count(c)
    return count


print(numJewelsInStones("aA", "aAAbbbbbb"))


# Another variant is to create a set out of the J


def numJewelsInStonesSet(J: str, S: str) -> int:
    count = 0
    unique = list(set(J))
    for c in unique:
        count += S.count(c)
    return count


print(numJewelsInStonesSet("aA", "aAAbbbbbb"))


# And using string comprehension and runtime is 36ms

def numJewelsInStonesCom(J: str, S: str) -> int:
    unique = list(set(J))
    return len([c for c in S if c in unique])
