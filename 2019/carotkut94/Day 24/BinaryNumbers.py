"""
Problem description can be found at https://www.hackerrank.com/challenges/30-binary-numbers/problem

Aurthor Sidhant Rajora
"""


n = int(input())
max_count = 0
one_count = 0

while n>0:
    factor = n // 2
    rem = n - 2 * factor
    n = factor
    if rem == 1:
        one_count += 1
        max_count = max(max_count,one_count)
    else:
        one_count = 0
print(max_count)
