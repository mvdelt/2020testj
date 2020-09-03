'''
# i. 2020.08.24.) 백준 '나무 자르기' 문제. 시간초과로 실패. 
#  ->다른사람들 풀이 보니까, 내방식이랑 비슷한데, 좀 더 스마트하게해서 바이너리서치보다 훨더빠르게 햇네.
#    나랑비슷한데, 나처럼 하나하나 더해가는방식 아니고, 넓이구하는방식.

예제입력
4 7   ->나무의 수 N, 가져가야하는길이 M.
20 15 10 17 ->나무의 높이들.
예제출력
15
'''
(N, M) = (int(w) for w in input().split())
hlist = sorted([int(w) for w in input().split()], reverse=True)+[0] # hlist의 인덱스 벗어나는에러 해결위해 +[0].

# hlist = sorted(list(map(int, input().split())), reverse=True)+[0] # 이렇게 바꿔도 시간초과네.

i, j = 0, 0 # i: 젤긴나무부터 0,1,.. j:젤긴나무를 1만큼자르는것부터 2,3,..
gsum = 0 # 가져갈 나무 길이 총합.
H = hlist[0] # 가장 긴 나무의 길이.
while not gsum>=M:
    while (not j+hlist[i] > H) and (not gsum>=M):
        j+=1
        gsum+=i    
    while (j+hlist[i]==H+1) and (not gsum>=M):
        i+=1
        gsum+=1
print(H-j)






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



