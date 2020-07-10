def dudu(*a):
    print(type(a))
    print(a)

def kuku(**d):
    print(type(d))
    print(d)

def mixj(*a,**d):
    print(a)
    print(set(a))
    print(d)
    print(set(d))

if __name__ == "__main__":
    # dudu([3,5,7],[33,44],{'dave':'yes','mak':'good'})
    # kuku(hi='yes', go='good', agej = 333)
    mixj(55,66,88,4,5,6,6,7, mixj='hoho', yow='man', num=55, nn = 101, greatj='fightingjj')