"""
카카오 2020블채기출 '기둥과 보'.
->전날인가 좀 생각하다 포기햇는데, 오늘(2020.09.10.목욜.) 다시해서 3시간좀넘게걸려서 품;; 풀고보니 걍 별거아니네;; 구현만 해주면 되는거네;;;
디자인: 
구현: 
"""
class GidungBo:
    # grid 에 write 하는 함수.
    def grWrite(self, x,y,item,what):
        n=self.n
        yg=n-y
        if item==0: # 기둥이면,
            if what==0: # 삭제면,
                self.grid[yg][x]-=1 # 기둥삭제: -1
                self.added.remove([x,y,item])
            else: # 추가면,
                self.grid[yg][x]+=1 # 기둥추가: +1
                self.added.append([x,y,item])
        else: # 보면,
            if what==0: # 삭제면,
                self.grid[yg][x]-=2 # 보삭제: -2
                self.added.remove([x,y,item])
            else: # 추가면,
                self.grid[yg][x]+=2 # 보추가: +2
                self.added.append([x,y,item])
        # print('after write:',self.grid)


    # grid 값을 read 하는 함수.
    def grRead(self, x,y):
        n=self.n
        yg=n-y
        try:
            return self.grid[yg][x]
        except IndexError:
            return -10 # grid 벗어난경우 -10 리턴.            


    # 주어진 아이템(기둥or보) 가 유효한지 체크하는 함수.
    def itemck(self, x,y,item):
        if item==1: # 보면,
            d,rd=self.grRead(x,y-1),self.grRead(x+1,y-1)       
            # print(f'{(x,y,item)}: d:{d}, rd:{rd}')     
            con1 = (d!=-1 and d!=1) or (rd!=-1 and rd!=1) # 한쪽 끝 부분이 기둥 위에 있거나,
            l,r=self.grRead(x-1,y),self.grRead(x+1,y)
            con2 = (l==1 or l==2) and (r==1 or r==2) # 또는, 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야.
            return con1 or con2
        else: # 기둥이면,
            con1 = y==0 # 바닥 위에 있거나,
            c,l=self.grRead(x,y),self.grRead(x-1,y)
            con2 = c==1 or c==2 or l==1 or l==2 # 보의 한쪽 끝 부분 위에 있거나,
            d = self.grRead(x,y-1)
            con3 = d==0 or d==2 # 또는, 다른 기둥 위에 있어야.
            return con1 or con2 or con3


    # 기둥/보 삭제후 유효한지 체크, 유효x시 삭제했던것 복구.
    def delck(self, x,y,item):
        # 삭제 수행.
        self.grWrite(x,y,item,0)        

        # if item==1: # item이 보면,
        #     # 체크해야할 아이템들: 좌보(x-1,y,1), 우보(x+1,y,1), 기둥(x,y,1), 우기둥(x+1,y,1).
        #     con = self.itemck(x-1,y,1) and self.itemck(x+1,y,1) and self.itemck(x,y,1) and self.itemck(x+1,y,1)        
        # else: # item이 기둥이면,
        #     # 체크해야할 아이템들: 상좌보(x-1,y+1,1), 상보(x,y+1,1), 상기둥(x,y+1,0).
        #     con = self.itemck(x-1,y+1,1) and self.itemck(x,y+1,1) and self.itemck(x,y+1,0)

        # 놓치고있는게 있는듯;; 걍 다 체크해보자. ->이렇게하니 되네;; 위의조건으로 부족한가봄;;
        con = True
        for i in self.added:
            if not self.itemck(*i):
                con = False
                break

        # if con:
        #     return con
        # else: # 삭제불가면,
        #     self.grWrite(x,y,item,1) # 삭제했던거 다시 복구.
        #     return con
        return con or self.grWrite(x,y,item,1)


    # 기둥/보 추가후 유효한지 체크, 유효x시 추가했던것 삭제.
    def addck(self, x,y,item):
        # add 수행.
        self.grWrite(x,y,item,1)
        # add 가능한지 체크, 불가시 add했던거 삭제.
        # print(f'{(x,y,item)} is {self.itemck(x,y,item)}')
        return self.itemck(x,y,item) or self.grWrite(x,y,item,0)


    def solution(self, n, build_frame):
        self.n=n
        N=n+1
        # 없음:-1, 기둥:0(-1+1), 보:1(-1+2), 둘다:2(-1+1+2)
        self.grid=[[-1]*N for _ in range(N)] # i. [[-1]*N]*N 으로 하면 안된다!!!!!!! 일케하면 '똑같은'놈이 복제되는거라, 한놈 바꾸면 모든놈이 다 바뀐다!!!!!!
        self.added = []        

        # 주어진 build_frame 의 각 원소에 대해 삭제/추가 진행.
        for i in build_frame:
            if i[3]==0:
                self.delck(i[0],i[1],i[2])
            else:
                self.addck(i[0],i[1],i[2])

        # 최종결과 정렬 후 리턴.
        ans = sorted(self.added)
        return ans



gb=GidungBo()
solution = gb.solution

n,bf = 5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n,bf = 5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
ret = solution(n, bf)
print(ret)
