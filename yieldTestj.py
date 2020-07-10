# def yftest():
#     # a = [5,6,7,8]
#     a = range(13,20)
#     print(a)
#     yield from a

# yf = yftest()
# print(next(yf))
# print(next(yf))
# print(next(yf))
# print(next(yf))

##############################################

li = [32,34,36,37,38,39]

def ytest():
    for idx, data in enumerate(li):
        yield [idx, data]

yt = ytest()
print(next(yt)[0], next(yt)[1])
print(next(yt))
print(next(yt))


# li2 = iter(li)
# print(next(li2))
# print(next(li2))
# print(next(li2))