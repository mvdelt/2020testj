"""
카카오2020.09.12.블채코테.6번문제.
15:33~
디자인: dp. 
"""
class SolClass:

    def nextPos(self, board,r,c):
        nextPosLi=[]
        #상: r-1
        if r>=1:
            nextPosLi+=[(r-1,c)]
        #하: r+1
        if r<=2:
            nextPosLi+=[(r+1,c)]
        #좌: c-1
        if c-1>=0:
            nextPosLi+=[(r,c-1)]        
        #우: c+1
        if c+1<=3:
            nextPosLi+=[(r,c+1)]

        #컨상
        _r=r
        if _r>=1:
            _r=_r-1        
        while _r>=1 and board[_r][c]==0:
            _r=_r-1
        if _r!=r: nextPosLi+=[(_r,c)]
        #컨하
        _r=r
        if _r<=2:
            _r=_r+1
        while _r<=2 and board[_r][c]==0:
            _r=_r+1
        if _r!=r: nextPosLi+=[(_r,c)]
        #컨좌
        _c=c
        if _c>=1:
            _c=_c-1        
        while _c>=1 and board[r][_c]==0:
            _c=_c-1
        if _c!=c: nextPosLi+=[(r,_c)]
        #컨우
        _c=c
        if _c<=2:
            _c=_c+1
        while _c<=2 and board[r][_c]==0:
            _c=_c+1
        if _c!=c: nextPosLi+=[(r,_c)]

        nextPosLi=list(set(nextPosLi))
        print(f'nextPosLi:{nextPosLi}')
        return nextPosLi


    def t(self, board,r,c,numRemain,selec,time):
        
        print(f'r,c,numRemain,time:{r},{c},{numRemain},{time}')

        if numRemain==0:
            return time

        # state: board, selec, r,c
        st_hash = hash(tuple([tuple(row) for row in board] + selec + [r,c]))
        if st_hash in self.st_hashes:
            return float('inf')
        self.st_hashes.add(st_hash)        

        # if board[r][c]:
        #     # if (r,c,0) in self.visited and (r,c,1) not in self.visited:
        #     #     return float('inf')
        #     if (r,c,1) in self.visited:
        #         return float('inf')
        # else:
        #     if (r,c,0) in self.visited:
        #         return float('inf')


        enterTimeLi=[]
        # r,c에 카드 있고, 이게 selec과 동일하고, 둘이 위치가 다를경우.
        if board[r][c] and board[r][c]==selec[2] and (r,c)!=(selec[0],selec[1]):
            print(f'r:{r}, c:{c}, board[r][c]:{board[r][c]}, self.selec:{selec}')
            # 엔터. => board 에서 두카드 모두 삭제.
            selec_r,selec_c=selec[0],selec[1]
            board[r][c]=0; board[selec_r][selec_c]=0
            _selec=[-1,-1,0] # selec은 다시 0으로.
            enterTimeLi+=[self.t(board,r,c,numRemain-2,_selec,time+1)]
            # return self.t(board,r,c,numRemain-2,_selec,time+1)
        
        # # r,c에 카드 있고, selec카드 있고, 둘이 다를경우.
        # if board[r][c] and self.selec[2] and board[r][c]!=self.selec[2]:
        #     pass # =>아무것도 안함.

        # r,c에 카드 있고, select카드 없을경우.
        if board[r][c] and selec[2]==0:
            _selec=[r, c, board[r][c]] # 엔터. selec 지정.
            enterTimeLi+=[self.t(board,r,c,numRemain,_selec,time+1)]
            # return self.t(board,r,c,numRemain,_selec,time+1)

        # print(self.nextPos(board,r,c))

        print(f'for nextPos - r:{r},c:{c}')
        print(f'enterTimeLi:{enterTimeLi}')
        npLi=self.nextPos(board,r,c)
        moveTimeLi=[self.t(board,rn,cn,numRemain,selec,time+1) for (rn,cn) in npLi]
        print(f'moveTimeLi:{moveTimeLi}')
        return min(enterTimeLi + moveTimeLi)

            


        
        


    def sol(self, board,r,c):
        selec=[-1,-1,0] # r,c,카드종류.
        # self.visited=set()
        self.st_hashes=set()

        nR = sum(1 for row in board for i in row if i)

        return self.t(board, r,c, numRemain=nR, selec=selec, time=0)


solcl=SolClass()
solution=solcl.sol

r_ex, c_ex, board_ex = 1, 0, [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
# r_ex, c_ex, board_ex = 0, 1, [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
# r_ex, c_ex, board_ex = 0, 0, [[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]]
ret=solution(board_ex, r_ex, c_ex)
print('ret:',ret)