n=int(input())
for i in range (0,n):
       n,k=map(int,input().split())
       l=[]
       for j in range(0,n):
              left,right=map(int,input().split())
              l.append([left,right])
       count=0
       for k in range(0,len(l)-1):
              for u in range(k+1,len(l)):
                     x=min(l[k][1],l[u][1])
                     xx=max(l[k][0],l[u][0])
                     diff=x-xx+1
                     if diff>count:
                            count=diff
       print(count)
                     
              
              
       
