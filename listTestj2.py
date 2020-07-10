# numlist = [3,4,5,6,7,8]
# a,*b,c,d = numlist
# print(a,b,c,d)

###############################################

# opt = False
# litest = [4,5,6,7 if opt else 'hahahah',8,9,10]
# print(litest)

################################################

li1 = [1,2,3,4,5]

li2 = ["idx:{}, item:{}".format(idx, item) for idx, item in enumerate(li1)] # i. 잘 되네! 리스트 컴프리헨션에서 enumerate 사용가능하네. 그리고 요정도 형식은 걍 파이썬에서 자동으로 형변환 해주나봄.

print(li2)