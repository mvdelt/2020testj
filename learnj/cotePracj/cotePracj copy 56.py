"""
카카오 2020블채기출 '블록 이동하기'.
디자인: dp 로 하면 될듯. 
구현: 
"""

class Move:

    def visitck(self, x1,y1,x2,y2): # 해당위치가 방문했던위치인지 여부 리턴.
        return (x1,y1,x2,y2) in self.visited or (x2,y2,x1,y1) in self.visited


    def t(self, x1,y1, x2,y2, sec): # x1,y1,x2,y2 지점에서 (N,N)위치까지 최소시간 리턴.
        
        memo=self.memo
        N=self.N

        if self.visitck(x1,y1,x2,y2):
            return float('inf')

        self.visited.add((x1,y1,x2,y2))
        print('visited:',self.visited)


        # if x1,y1 또는 x2,y2 가 이미 도착이면:
        if (x1,y1)==(N-1,N-1) or (x2,y2)==(N-1,N-1):
            return sec

        if (x1,y1,x2,y2) in memo or (x2,y2,x1,y1) in memo:
            return memo[x1,y1,x2,y2]

        li = [self.t(x1a,y1a,x2a,y2a, sec+1) for x1a,y1a,x2a,y2a in self.nextPos(x1,y1,x2,y2)]
        if len(li)!=0:
            memo[x1,y1,x2,y2] = min(li)
        else:
            return float('inf')
        # memo[x1,y1,x2,y2] = min(self.t(x1,y1, x2,y2, sec+1) for x1,y1,x2,y2 in self.nextPos(x1,y1,x2,y2))
        # hubos=[]
        # print(self.nextPos(x1,y1,x2,y2))
        # for x1a,y1a,x2a,y2a in self.nextPos(x1,y1,x2,y2):
        #     hubos+=[self.t(x1a,y1a, x2a,y2a, sec+1)]
        # memo[x1,y1,x2,y2] = min(hubos)

        return memo[x1,y1,x2,y2]
    

    # 지금 nextPos 함수가 뭔가 이상한듯...

    def nextPos(self, x1,y1,x2,y2): # 1초뒤 가능한 포지션들의 리스트 리턴.
        board = self.board
        visited = self.visited
        N = self.N
        nextPosLi = []
        print(f'in nextPos, x1,y1,x2,y2:{x1},{y1},{x2},{y2}')
        # 상하좌우이동.
        for tup in [(x1-1,y1,x2-1,y2), (x1+1,y1,x2+1,y2), (x1,y1-1,x2,y2-1), (x1,y1+1,x2,y2+1)]:
            print(f'tup:{tup}')
            for loc in tup:
                print(f'loc:{loc}')
                if loc==-1 or loc==N: # 이부분... 뭔가 의도와 다르게 되고잇다.. 
                    break
            else: # if not break
                x1a,y1a,x2a,y2a=tup[0],tup[1],tup[2],tup[3]
                print(f'x1,y1,x2,y2: {x1a},{y1a},{x2a},{y2a}')
                if board[x1a][y1a]==0 and board[x2a][y2a]==0:
                    nextPosLi+=[(x1a,y1a,x2a,y2a)]

        print(f'befor rotatation, nextPosLi:{nextPosLi}')

        # 회전.        
        if x1==x2: # 로봇이 가로방향일경우.
            if x1-1!=-1 and board[x1-1][y1]==0 and board[x2-1][y2]==0: # 윗줄이 보드안이고 두칸다 비어있을경우(에만 윗회전가능).
                if y1<y2:
                    nextPosLi+=[(x1-1,y1+1,x2,y2), (x1,y1,x2-1,y2-1)]
                else:
                    nextPosLi+=[(x1-1,y1-1,x2,y2), (x1,y1,x2-1,y2+1)]

            if x1+1!=N and board[x1+1][y1]==0 and board[x2+1][y2]==0: # 아랫줄이 보드안이고 두칸다 비어있을경우(에만 아래회전가능).
                if y1<y2:
                    nextPosLi+=[(x1+1,y1+1,x2,y2), (x1,y1,x2+1,y2-1)]
                else:
                    nextPosLi+=[(x1+1,y1-1,x2,y2), (x1,y1,x2+1,y2+1)]

        
        if y1==y2: # 로봇이 세로방향일경우.
            if y1-1!=-1 and board[x1][y1-1]==0 and board[x2][y2-1]==0: # 왼쪽줄이 보드안이고 두칸다 비어있을경우(에만 좌회전가능).
                if x1<x2:
                    nextPosLi+=[(x1+1,y1-1,x2,y2), (x1,y1,x2-1,y2-1)]
                else:
                    nextPosLi+=[(x1-1,y1-1,x2,y2), (x1,y1,x2+1,y2-1)]

            if y1+1!=N and board[x1][y1+1]==0 and board[x2][y2+1]==0: # 오른쪽줄이 보드안이고 두칸다 비어있을경우(에만 우회전가능).
                if x1<x2:
                    nextPosLi+=[(x1+1,y1+1,x2,y2), (x1,y1,x2-1,y2+1)]
                else:
                    nextPosLi+=[(x1-1,y1+1,x2,y2), (x1,y1,x2+1,y2+1)]


        print(f'nextPosLi:{nextPosLi}')
        return nextPosLi
            
                            



    def sol(self, board):
        self.visited = set()
        self.memo = {}
        self.board = board
        self.N = len(board)
        
        ret = self.t(0,0,0,1, sec=0)
        print('memo:',self.memo)
        return ret



board_ex = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
mv = Move()
ret = mv.sol(board_ex)
print('ret:',ret)