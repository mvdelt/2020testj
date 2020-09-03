'''
# i. 2020.08.24.) 백준 '나무 자르기'  *솔루션2*. 통과함.
예제입력
4 7   ->나무의 수 N, 가져가야하는길이 M.
20 15 10 17 ->나무의 높이들.
예제출력
15
'''

# i. 첫번째솔루션이 시간초과돼서 걍 바이너리서치 방법으로 해보려함.
# 바이너리서치로 하면 time complexity는 O(N*logN) 일것으로 생각됨.
# 근데, 첫번째솔루션도 time complexity는 O(N*logN) 일것같은데 왜냐면 sorting하는게 오래걸리지 그이후 탐색은 O(N)일거거든.
# 암튼 일케하니까 통과하긴 하네?;;;;

def ok(cuth): # 취하게될 나무길이 합이 M이상인지를 리턴.
    return sum([h-cuth for h in hs if h-cuth>0])>=M

(N, M) = (int(w) for w in input().split())
hs = list(map(int, input().split()))
low, high = 0, max(hs)

while low<high:
    mid = (low+high)//2
    if ok(mid):
        low = mid+1
    else:
        high = mid
print(low-1)








# hlist = sorted([int(w) for w in input().split()], reverse=True)+[0] # hlist의 인덱스 벗어나는에러 해결위해 +[0].

# i, j = 0, 0 # i: 젤긴나무부터 0,1,.. j:젤긴나무를 1만큼자르는것부터 2,3,..
# gsum = 0 # 가져갈 나무 길이 총합.
# H = hlist[0] # 가장 긴 나무의 길이.
# while not gsum>=M:
#     while (not j+hlist[i] > H) and (not gsum>=M):
#         j+=1
#         gsum+=i    
#     while (j+hlist[i]==H+1) and (not gsum>=M):
#         i+=1
#         gsum+=1
# print(H-j)






# H = hlist[0] # i. 가장 긴 나무의 길이.

# sumj = 0
# j=1
# for y in range(N):
#     if not j+hlist[y] > H:
#         j = H-hlist[y]+1
#     sumj+=j-1
#     if (y+1)*j-sumj >= M:
#         break
    


#     if y+1+hlist[y] > H:
#         sumj+=y

# # H = hlist[0] # i. 가장 긴 나무의 길이.
# # for x in range (1, H+1):
# #     for h in hlist:
# #         if x+h > H:







# H = hlist[0] # i. 가장 긴 나무의 길이.

# NH = []
# for h in hlist:
#     t = [0]*H
#     t[H-h:] = [i for i in range(1, h+1)]
#     NH += [t]



