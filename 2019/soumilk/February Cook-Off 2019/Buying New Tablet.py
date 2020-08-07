n=int(input())
for i in range(0,n):
       num,bug=map(int,input().split())
       resultant=[]
       flag=0
       for j in range(0,num):
              w,h,p=map(int,input().split())
              resultant.append([w*h,p])
       resultant.sort(reverse=True)
       for k in resultant:
              if k[1]<=bug:
                     print(k[0])
                     flag=1
                     break
       if flag==0:
              print("no tablet")
              
#resultant.sort(reverse=True)
#print(resultant)
