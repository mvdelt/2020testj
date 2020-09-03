'''
# i. 2020.08.26.) 백준 '구슬탈출2' 문제. ->일단 테스트케이스들은 모두 통과. 오오 제출도 통과!!!
#                ->만약 시간초과였다해도, 시행착오거의안거치고 머릿속구상대로 제대로 구현했다는것이 맘에듦.

입력
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 
다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. 
'.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다.
'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 
구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

출력
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 
만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
'''
# i. DP 방식으로 풀어볼생각임.
# state: 구슬들의 위치.

# 이미 진행중인 state인지 확인위해, state들을 해시화하여 보관.
# {state해시값1: 이동횟수, ..} 이런식. 이동횟수 더 적은경우 생기면 덮어씌움.
state_hashed = {}

# n: 이동횟수. 0부터 입력.
def sol(state, n): # 입력된 state에서 최소이동횟수 리턴.
    # state값이 None이면, 진행 무의미.
    if state == None:
        print(f'state is None, return inf. state:{state}, n:{n}')
        return float('inf')
    # n이 10 초과시, 진행 무의미.
    if n>10:
        print(f'n>10, return inf. n:{n}')
        return float('inf')

    # state, n 을 state_hashed에서 비교.
    ## 같은 state가, 같거나 더 작은 n값으로 존재하면, 진행 무의미. 
    ## 기록된 state가 없거나, 같은 state가 있더라도 지금의 n값이 더 작으면, 기록or덮어씌움. 
    if hash(state) in state_hashed:
        if state_hashed[hash(state)] <= n:
            print(f'state already searched. return inf.')
            return float('inf')
    else:
        state_hashed[hash(state)] = n

    # 현재상태가 탈출상태면,
    if check_state(state)==0:
        print(f'fin state. return n. n:{n}, state:{state}')
        return n
    # B가 빠졌으면, 진행 무의미.
    if check_state(state)==1:
        print(f'B is in hole. return inf. state:{state}')
        return float('inf')
    # R,B 둘다남은상태면,
    return min(sol(r(state), n+1), sol(l(state), n+1), sol(u(state), n+1), sol(d(state), n+1))
    
def check_state(state): # state: (R좌표, B좌표) <-만약 홀에빠졋으면 좌표값은 튜플아닌 그냥 숫자 0.
    # 탈출상태면 0, B가 빠졋으면 1, R과B둘다남았으면 2 리턴.
    if state[1]==0:
        return 1
    if state[0]==0:
        return 0
    return 2

def r(state): # 우 이동. 이동 후의 state를 r_state로 바인딩.
    state_li = [[state[0][0],state[0][1]],[state[1][0],state[1][1]]]
    # while R우측이 '.':
    while mapj[state_li[0][0]][state_li[0][1]+1] == '.':
        state_li[0][1]+=1
    # while B우측이 '.':
    while mapj[state_li[1][0]][state_li[1][1]+1] == '.':
        state_li[1][1]+=1
    # if R우측이 'O':
    if mapj[state_li[0][0]][state_li[0][1]+1] == 'O':
        state_li[0]=0
    # if B우측이 'O':
    if mapj[state_li[1][0]][state_li[1][1]+1] == 'O':
        state_li[1]=0
    # RB겹쳤을경우 이동 전 위치정보 이용하여 늦은구슬을 한칸 빼줌.
    if state_li[0]==state_li[1] and state_li[0]!=0: 
        if state[0][1]>state[1][1]:
            state_li[1][1]-=1
        else:
            state_li[0][1]-=1
    r_state = tuple(tuple(i) if i!=0 else i for i in state_li) # list of list 를 tuple of tuple로 변환 (만약0이면 그대로 0으로).

    # 구슬들의 위치 변화 있으면, 위치 리턴. 
    if state!=r_state:
        return r_state
    # 바뀐게없으면 None 리턴.(이거안써줘도 저절로 None이 리턴되긴하지만.)
    return None

def l(state): # 좌 이동. 이동 후의 state를 r_state로 바인딩.
    state_li = [[state[0][0],state[0][1]],[state[1][0],state[1][1]]]
    # while R좌측이 '.':
    while mapj[state_li[0][0]][state_li[0][1]-1] == '.':
        state_li[0][1]-=1
    # while B좌측이 '.':
    while mapj[state_li[1][0]][state_li[1][1]-1] == '.':
        state_li[1][1]-=1
    # if R좌측이 'O':
    if mapj[state_li[0][0]][state_li[0][1]-1] == 'O':
        state_li[0]=0
    # if B좌측이 'O':
    if mapj[state_li[1][0]][state_li[1][1]-1] == 'O':
        state_li[1]=0
    # RB겹쳤을경우 이동 전 위치정보 이용하여 늦은구슬을 한칸 뒤로해줌.
    if state_li[0]==state_li[1] and state_li[0]!=0: 
        if state[0][1]>state[1][1]:
            state_li[0][1]+=1
        else:
            state_li[1][1]+=1
    r_state = tuple(tuple(i) if i!=0 else i for i in state_li) # list of list 를 tuple of tuple로 변환 (만약0이면 그대로 0으로).

    # 구슬들의 위치 변화 있으면, 위치 리턴. 
    if state!=r_state:
        return r_state
    # 바뀐게없으면 None 리턴.(이거안써줘도 저절로 None이 리턴되긴하지만.)
    return None


def u(state): # 위 이동. 이동 후의 state를 r_state로 바인딩.
    state_li = [[state[0][0],state[0][1]],[state[1][0],state[1][1]]]
    # while R위가 '.':
    while mapj[state_li[0][0]-1][state_li[0][1]] == '.':
        state_li[0][0]-=1
    # while B위가 '.':
    while mapj[state_li[1][0]-1][state_li[1][1]] == '.':
        state_li[1][0]-=1
    # if R위가 'O':
    if mapj[state_li[0][0]-1][state_li[0][1]] == 'O':
        state_li[0]=0
    # if B위가 'O':
    if mapj[state_li[1][0]-1][state_li[1][1]] == 'O':
        state_li[1]=0
    # RB겹쳤을경우 이동 전 위치정보 이용하여 늦은구슬을 한칸 빼줌.
    if state_li[0]==state_li[1] and state_li[0]!=0: 
        if state[0][0]>state[1][0]:
            state_li[0][0]+=1
        else:
            state_li[1][0]+=1
    r_state = tuple(tuple(i) if i!=0 else i for i in state_li) # list of list 를 tuple of tuple로 변환 (만약0이면 그대로 0으로).

    # 구슬들의 위치 변화 있으면, 위치 리턴. 
    if state!=r_state:
        return r_state
    # 바뀐게없으면 None 리턴.(이거안써줘도 저절로 None이 리턴되긴하지만.)
    return None


def d(state): # 아래 이동. 이동 후의 state를 r_state로 바인딩.
    state_li = [[state[0][0],state[0][1]],[state[1][0],state[1][1]]]
    # while R아래가 '.':
    while mapj[state_li[0][0]+1][state_li[0][1]] == '.':
        state_li[0][0]+=1
    # while B아래가 '.':
    while mapj[state_li[1][0]+1][state_li[1][1]] == '.':
        state_li[1][0]+=1
    # if R아래가 'O':
    if mapj[state_li[0][0]+1][state_li[0][1]] == 'O':
        state_li[0]=0
    # if B아래가 'O':
    if mapj[state_li[1][0]+1][state_li[1][1]] == 'O':
        state_li[1]=0
    # RB겹쳤을경우 이동 전 위치정보 이용하여 늦은구슬을 한칸 빼줌.
    if state_li[0]==state_li[1] and state_li[0]!=0: 
        if state[0][0]>state[1][0]:
            state_li[1][0]-=1
        else:
            state_li[0][0]-=1
    r_state = tuple(tuple(i) if i!=0 else i for i in state_li) # list of list 를 tuple of tuple로 변환 (만약0이면 그대로 0으로).

    # 구슬들의 위치 변화 있으면, 위치 리턴. 
    if state!=r_state:
        return r_state
    # 바뀐게없으면 None 리턴.(이거안써줘도 저절로 None이 리턴되긴하지만.)
    return None



# 콘솔 입력값 받기.
H, W = map(int, input().split())
state_li = [None, None]
map_li = []
for rowdx in range(H):
    rowstr = input()
    if 'R' in rowstr:
        state_li[0] = (rowdx, rowstr.index('R'))
        rowstr = rowstr.replace('R','.')
    if 'B' in rowstr:
        state_li[1] = (rowdx, rowstr.index('B'))
        rowstr = rowstr.replace('B','.')
    map_li.append(tuple(rowstr))
state = tuple(state_li)
mapj = tuple(map_li)
print(f'mapj:{mapj}')


# sol함수 실행!
ret = sol(state, 0)
if ret == float('inf'):
    print(-1)
else:
    print(ret)