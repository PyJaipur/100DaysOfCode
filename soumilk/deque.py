'''
In this code, implementation of the deque is depicted, the methods of the deque can be many more, few of them are listed in this code.   
'''
from collections import deque
de=deque([5,4,3,2,1])
de.remove(5)
print("after remove" ,de)
de.append(12)
print("append ", de)
de.appendleft(9)
print("appendleft ", de)
de.pop()
print("pop ",de)
de.popleft()
print("popleft ",de)
print("count of 2  ",de.count(2))
de.reverse()
print("reverse ",de)

# Output :
''''
after remove deque([4, 3, 2, 1])
append  deque([4, 3, 2, 1, 12])
appendleft  deque([9, 4, 3, 2, 1, 12])
pop  deque([9, 4, 3, 2, 1])
popleft  deque([4, 3, 2, 1])
count of 2   1
reverse  deque([1, 2, 3, 4])
''' 
