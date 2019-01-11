## Fast exponentiation :
usually in competitions, we need to calculate the large exponential powers of the numbers and we need to find out the values.<br>
To calculate the exponentials of a given number, the naive approach is to simple run the loop and multiply the digit exponent times <br>
### Code example of naive approach ( O(n) ):<br>
this algo will take the time propotional to the exponent number. In most of the coding contests, this approach to find out the exponential <br>
will give a TLE (time limit exceed).
```
def exponent(a,n):
       ans=1
       if n==0:
              return 1
       elif n==1:
              return a
       for i in range(0,n):
              ans=ans*a
       return ans
```
Now we will discuss the better and the fast approach to get the exponent of the number.
### Code example of fast approach ( O(log n) ): <br>
This is the fast and a better way to find out the exponentials of the number, it basically keeps slicing the exponent by half till <br>
it becomes 1 or 0.

```
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
```

