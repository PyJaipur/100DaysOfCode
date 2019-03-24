# It is always important to close the file you open
# we usually use context managers to read and write files.

'''
f=open('test.txt','r+')
print(f.name)
print(f)
print(f.mode)
print(f.read()) # It reads all the contents of the file
f.close()
'''

# It allows to work with files within a block and as soon as the block is over the file is automatically closed

with open('test.txt','r') as f:    # file open in read mode
       print(f.readlines())
       print()
       f.seek(0)                   # Set the reader on index 0
       print(f.readline(),end="")  # Read a single line
       print(f.readline(),end="")
       f.seek(0)
       print("\nWITH LOOP")
       for i in f:
              print(i,end='')

       f.seek(0)
       print(f.readline())
       f.seek(0)
       print(f.readline(3))        # upto what idex you want to read
       print(f.tell())             # Denotes the current position
       pass

print(f.closed)                    # this will give us a bool value i.e True

# print(f.read()) ->  This will give an error as we are trying to access file when it is closed
