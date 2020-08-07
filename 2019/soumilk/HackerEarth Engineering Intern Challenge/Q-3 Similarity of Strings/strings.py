t=int(input())
for y in range(0,t):
       s=input()
       sub=input()
       start=[]
       x=s.count(sub[0])
       start.append(s.find(sub[0]))
       #print(start,x)
       count=[]
       j=1
       f=0
       k=1
       if sub in s:
              print("Yes")
              print(0)
              continue
       else:
              for i in range(0,x):
                     for j in range(start[i]+1,len(s)):
                            #print("j ",j, "  k ",k) 
                            if k>=len(sub):
                                   break
                            if s[j]==sub[k]:
                                   k+=1
                                   continue
                            if s[j]!=sub[k]:
                                   f+=1
                                   continue
                            
                     if len(s)-start[i]>=len(sub) and k>=len(sub):
                          count.append(f)
                     f=0
                     k=1
                     #print("count " ,count)
                     start.append(s.find(sub[0],start[i]+1))

       count.sort()
       if len(count)==0:
              print("No")
       else:
              print("Yes")
              print(count[0])
