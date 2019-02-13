class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

n,k=[int(x) for x in input().split()]

d={}

path=[0]*(int(n)+1)
sum1=0
sum2=0

root,first=[int(x) for x in input().split()]
d["a"+str(root)]=Node(root)
d["a"+str(first)]=Node(first)
if(d["a"+str(root)].left==None):
	d["a"+str(root)].left=d["a"+str(first)]
else:
	d["a"+str(root)].right=d["a"+str(first)]


for i in range(int(n)-2):
	f,g=[int(x) for x in input().split()]
	d["a"+str(g)]=Node(g)
	if(d["a"+str(f)].left==None):
		d["a"+str(f)].left=d["a"+str(g)]
	else:
		d["a"+str(f)].right=d["a"+str(g)]

def Inorder(node):
	global sum2
	if node:
		sum2+=1
		Inorder(node.left)
		Inorder(node.right)
	return sum2

for i in range(int(k),int(n)+1):
	sum2=0
	path[i]=Inorder(d["a"+str(i)])-1
	sum1+=path[i]

print(sum1)
