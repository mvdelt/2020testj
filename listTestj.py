# Initialize the zero-valued list with 100 length
zeros_list = [0] * 5
print(zeros_list)

# Declare the zero-valued tuple with 100 length
zeros_tuple = (0,) * 8  
print(zeros_tuple)

# Extending the "vector_list" by 3 times
vector_list = [[1, 2, 3]] 
print(vector_list*4)


# for i, vector in enumerate(vector_list * 3):     
#     print("{0} scalar product of vector: {1}".format((i + 1), [(i + 1) * e for e in vector]))
# 1 scalar product of vector: [1, 2, 3]
# 2 scalar product of vector: [2, 4, 6]
# 3 scalar product of vector: [3, 6, 9]