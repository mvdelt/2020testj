li = [2,3,3,4,5,6,7]
li2 = [[4,5],[6,7],[8,9],[8,9]]

print(set(li))
# print(set(li2)) # TypeError: unhashable type: 'list'
print({tuple(i) for i in li2})
print(type({tuple(i) for i in li2}))


print(li.count(3))

print(list(li))

for i in list(li):
    li.remove(i) # i. 같은게 여러개잇으면 첫번째원소만 삭제함.

print(li)


