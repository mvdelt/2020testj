coordinate = ['x', 'y', 'z' , 'a' , 'b', 'c']
value = [3, 4, 5, 6, 7]

result = zip(coordinate, value)

for idx, (c, v) in enumerate(zip(coordinate, value)):
    print('idx:',idx)
    print('c:',c)
    print('v:',v)

# result_list = list(result)
# print(result_list)
# print(*result_list)

# c, v =  zip(*result_list)

# print('c =', c)
# print('v =', v)