from itertools import product
a = list(product(list(range(1,10)), repeat=3)) # [(2,2,3), (5,9,1), ...]
a = product(list(range(1,10)), repeat=3) # [(2,2,3), (5,9,1), ...]
a = list(product(range(1,10), repeat=3)) # [(2,2,3), (5,9,1), ...]


# print(a)


from itertools import product
prodTup_list = list(product(range(1,10), repeat=3)) # [(1,1,1), (1,1,2), (1,1,3), ...]
prod_list = []
for prodTup in prodTup_list:
    prodStr = ''
    for i in prodTup:
        prodStr += str(i)
    prod_list.append(int(prodStr))
# -> prod_list = [111, 112, 113, ...]

# print(len(prod_list))
# print(prod_list)


from itertools import permutations
prodTup_list = list(permutations(range(1,10), 3)) 

# print(prodTup_list)


a = [i for i in permutations(range(1,10), 3)]
# print('a:',a)
# print(list(permutations(range(1,10), 3)))


answer_list = {}
for i in [i for i in permutations(range(1,10), 3)]:
    answer_list['%s%s%s' %(i)] = [0, 0]
# print(answer_list)


# print('%s%s%s' %((2,4,5)))

# t = (1,3,4)
# print('{}'.format((1,3,3)))
# print(f'{t}')


baseball_ex1 = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

for a,b,c in baseball_ex1:
    print(a)

