da = {'a': 1, 'b': 2, 'c': 3, 'e': 7}
db = {'a': 4, 'b': 5, 'c': 6, 'd': 9}

print('set(da):', set(da))
print('set(db):', set(db))

dc = set(da) & set(db)

# print('dc:', dc)

# for i in dc:
#   print(i,da[i],db[i])

print([(a,b) for a,b in zip(da.items(), db.items())])
print([(a,b,c) for a,b,c in zip(da.keys(), da.values(), db.values())])

print('set(list):', set([1,2,3,4]))
# print('set(nums):', set(1,2,3,4)) # TypeError: set expected at most 1 arguments, got 4
# print('set(list):', {[1,2,3,4]}) # TypeError: unhashable type: 'list'
# print('set(int):', set(3)) # TypeError: 'int' object is not iterable
print('set(int):', {3})
print('type of set(int):', type({3}))

if []:
    print('yes')
else:
    print('no')

print(len({}))