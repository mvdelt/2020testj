num_list = [1,2,3,4,5]
name_list = ['aa','bb','cc','dd','ee']
list1 = [num_list, name_list]
print(*list1)
for i in zip(*list1):
    print(i)


