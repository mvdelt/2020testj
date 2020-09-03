def solution(numbers):
    # return str(int(''.join([str(i) for i in sorted(numbers, key=keyf, reverse=True)])))
    return ((' '.join([str(i) for i in sorted(numbers, key=keyf, reverse=True)])))

    
def keyf(num):  
    return [int(str(num)[i%len(str(num))]) for i in range(4)]


numbers_ex1 = [9,99,999, 991, 55,66,35 , 0, 100, 1000, 856, 855, 854, 888, 579,578,576,574,571,57,5,55,555,1,112,0,0,0,0]
numbers_ex2 = [0,0,0]
ret = solution(numbers_ex1)
print(ret)

# print(int('00000'))

print('str sort:', sorted(['123','1231','1241','1211199', '101010','100100100','100010001000'], reverse=True))