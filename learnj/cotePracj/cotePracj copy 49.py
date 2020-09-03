"""
2020.08.30.일욜아침. 백준 '정수 삼각형' 문제.
-> DP로 쉽게 품. 근데 구현까지 47분걸림;;;; 입력받는거 해보는데 20분넘게쓴듯;;; 더빨리해야한다!!!
"""

# 디자인: 1. DP. 2. DFS/BFS? 이건 왠지 안될것같다. 일단 DP먼저해보자.

class Triangle:
    def __init__(self):
        # 입력 저장.
        numLines = int(input())
        self.tri = []
        for rowdx in range(numLines):
            self.tri+=[list(map(int, input().split()))]
        # print(f'self.tri:{self.tri}')        

        # for memoization.
        self.memo={}
        
        # 메인함수 실행, 출력.
        print(self.maxsum(0,0))
        # print(f'self.memo:{self.memo}')

    def maxsum(self, rdx, cdx):
        if (rdx, cdx) in self.memo:
            return self.memo[rdx,cdx]        
        if rdx == len(self.tri)-1:
            return self.tri[rdx][cdx]
        self.memo[rdx,cdx] = ret = max(self.maxsum(rdx+1, cdx), self.maxsum(rdx+1, cdx+1)) + self.tri[rdx][cdx]
        return ret


# 클래스 호출.
Triangle()