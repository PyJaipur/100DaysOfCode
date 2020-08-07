n=int(input())
for i in range(0,n):
       arr=[]
       num=int(input())
       arr=list(map(int,input().split()))
       arr.sort()
       print(arr)
       count=0
       for j in range(0,len(arr)):
              if arr[j]==0:
                     count+=1
                     continue
              if count>=arr[j]:
                     count+=1
                     print(count)
       print(count)
              
