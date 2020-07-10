# from testDir.testChildDir.dirfile10 import fct10
# from testDir.testChildDir.testGrandChildDir.testSuperGrandChildDir import sgc, noman
from testDir.testChildDir.testGrandChildDir import testSuperGrandChildDir
# import testDir

# import test2j
# import test3j

if __name__ == '__main__':
    print('this is HOME - testj.py')
    # 만약 sgc.py가 임포트된거면: 아래는 실행되어야함. sgc()라고하면 sgc는 not callable 하다고 나올거임.
    # sgc.sgc()
    # 만약 sgc 함수가 임포트된거면: 아래는 실행되어야함. sgc.sgc()라고하면 sgc함수에 뭐 그런 속성? 이 없다고 나올듯?->맞음.
    # sgc()

    testSuperGrandChildDir.noman.nomanInside()
    testSuperGrandChildDir.noman.nomanInside()
    testSuperGrandChildDir.noman.nomanInside()
    testSuperGrandChildDir.sgc.sgc()
    testSuperGrandChildDir.sgc.sgc()
    testSuperGrandChildDir.sgc.sgc()
    # noman.nomanInside()