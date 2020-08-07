# this is the code to be tested in and it is divided into
# modules

def add(x,y):
       return x+y

def multiply(x,y):
       return x*y

def subtract(x,y):
       return x-y

def divide(x,y):
       if y==0:
              raise ValueError("can not divide by zero")
       return x/y
