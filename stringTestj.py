str1 = "my name is haha._crop great jun"
str2 = str1[:7] # "my name"
str3 = str1[:10] # "my name is"
print(str1) # i. str1 의 값은 변하지 않는다.
print(str2)
print(str3)

idx = str1.index('_crop') # i. .index는 .find 와 거의 같은데, .find는 못찾으면 -1을 반환하지만 .index는 못찾으면 에러띄움.
print(idx)
str1_cut = str1[:idx]
print(str1_cut)
print(str1)