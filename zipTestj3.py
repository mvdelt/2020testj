num_list = [1,2,3,4,5]
name_list = ['aa','bb','cc','dd','ee']

for en in enumerate(zip(num_list, name_list)):
    print('en:',en)

for idx, (num, name) in enumerate(zip(num_list, name_list)):
    print('idx:',idx)
    print('num:',num)
    print('name:',name)

for zip_elem in zip(num_list, name_list):
    print('zip_elem:',zip_elem)

for (a,b) in zip(num_list, name_list):
    print(a)
    print(b)