numbers = [3,5,6,7,9, 0]

numbers = [i if i!=0 else 11 for i in numbers]

# numbers = [i+2 for i in numbers  if i!=0]

print(numbers)


tup1 = (5,7,1,2); tup2 = (3,10,20,1)
# print( tup1-tup2) # i. TypeError
print(tuple(a-b for (a,b) in zip(tup1,tup2)))

seq=['l','r','r','l']
print(''.join(seq))

a = ''
print(a+'l'+'r')