# print(tuple([1,2,3,5]))

# for idx,i in enumerate(range(5)):
#     print(idx,i)

# for a,b in zip([1,2,3,4,5],[10,20]):
#     print(a+b)

# for i in range(10,-2,-1):
#     print(i)

# a = min(float('inf'), float('inf'))
# print(a)
# if a == float('inf'):
#     print('this is inf')

tup_tup = (((1,2),('3','4')),('3',5))
tup_tup2 = (((1,2),('3','4')),('3',5))
print(tup_tup)
print(type(tup_tup))
print(hash(tup_tup))
print(hash(tup_tup2))
print(hash(tup_tup))
print(hash(tup_tup2))
print(tuple('abchahajj'))
print(tuple('abchahajj'))

print(tuple([(1,2),(3,4)]))
print(list(((4,5),(6,3))))

a = [[1,3],[1,3]]
if a[0]==a[1]:
    print('they are same')
print(tuple(a))
# print(tuple(33)) # Error.

state_li = [[5,6],0]
r_state = tuple(tuple(i) if i!=0 else i for i in state_li)
print('type of r_state:',type(r_state))
print('r_state:',r_state)