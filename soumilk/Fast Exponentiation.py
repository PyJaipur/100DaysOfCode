
# Naive approach O(n)
def exponent(a,n):
       ans=1
       if n==0:
              return 1
       elif n==1:
              return a
       for i in range(0,n):
              ans=ans*a
       return ans

# fast exponentation O(log n)
def exponent1(a,n):
       if n==0:
              return 1
       elif n==1:
              return a
       else:
              r=exponent1(a,n//2)
              if n%2==0:
                     return r*r
              else:
                     return r*a*r

a=int(input("Enter the number "))
n=int(input("Enter the exponent "))
s1=exponent(a,n)
s=exponent1(a,n)
print(s1)
print(s)

