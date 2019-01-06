duplicate = eval(input("enter your array within []"))
duplicate.sort()
i = 0
while i < (len(duplicate)-1):
    if duplicate[i] == duplicate[i+1]:
        print("true")
        break   
    i = i+1
if i == (len(duplicate) - 1):
    print("false")
    
