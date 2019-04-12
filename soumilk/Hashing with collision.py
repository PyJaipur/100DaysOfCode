def hash_function(x):
       return x%10
def insert(hash_table,x,s):
       key=hash_function(x)
       hash_table[key].append(s)
       
hash_table=[[] for i in range (10)] 
print(hash_table)
insert(hash_table,19,"USA")
insert(hash_table,55,"India")
insert(hash_table,78,"Canada")
insert(hash_table,52,"Japan")
insert(hash_table,19,"russia")
insert(hash_table,55,"china")
insert(hash_table,78,"swedan")
insert(hash_table,52,"brazil")
print(hash_table)

if 'Japan' in hash_table[2]:
       print('found')
print(hash_table[2])

#output:
#[[], [], [], [], [], [], [], [], [], []]
#[[], [], ['Japan', 'brazil'], [], [],
# ['India', 'china'], [], [], ['Canada', 'swedan'],
# ['USA', 'russia']]
