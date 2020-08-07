#!/usr/bin/env python3

from math import sqrt

n=int(input())

a=[]
a.append(1)
flag=0
sum=1
for i in range(n-1):
	b=sqrt(sum)
	c=(b+1)*(b+1)
	if(int(c-sum)<=1000000):
		a.append(int(c-sum))
		sum+=a[i+1]
	else:
		flag=1

if(flag==1):
	print(-1)
else:
	for i in a:
		print(i,end=" ")
