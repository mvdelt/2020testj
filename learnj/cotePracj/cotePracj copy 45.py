'''
# i. 2020.08.25.) 백준 '개똥벌레' 문제.
입력
첫째 줄에 N과 H가 주어진다. N은 항상 짝수이다. (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000)
다음 N개 줄에는 장애물의 크기가 순서대로 주어진다. 장애물의 크기는 H보다 작은 양수이다.

출력
첫째 줄에 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 공백으로 구분하여 출력한다.
'''
# # i. 내 첫 솔루션. 엄청 잘푼줄 알앗는데 시간초과;; 
# # 그도그럴것이, time complexity가 최소 O(N*H) 인것같음(더하는과정만쳐도). 
# N, H = tuple(map(int, input().split()))
# sumj = [0]*H
# for i in range(N):
#     h = int(input())
#     if i%2==0:
#         sumj = [a+b for a, b in zip(sumj, [1]*h+[0]*(H-h))]
#     else:
#         sumj = [a+b for a, b in zip(sumj, [0]*(H-h)+[1]*h)]
# print(min(sumj), sumj.count(min(sumj)))

# i. 이문제가 prefix sum 방식을 쓰면 된다는 글을 보고 생각한 솔루션.
# 대충 생각해봐도, 이방식은 time complexity가 O(N+H) 정도다(더하는과정까지는).
# -> 이것도 시간초과;;
#    생각해보니, for문에서 la,ra구할때 불필요하게 중복되는 더하기연산을 하고잇고, ->요건수정함.
#    최솟값 구하면서 바로 갯수 카운팅할수잇는데 최솟값따로,갯수따로 구하고잇는 문제가 일단 잇네.
#    지금 자야돼서 낼 생각하자;;
N, H = tuple(map(int, input().split()))
l=[0]*H
r=[0]*H
for i in range(N):
    h = int(input())
    if i%2==0:
        l[h-1]+=1
    else:
        r[-h]+=1

for i in range(H-2, -1, -1):
    l[i]+=l[i+1]
for i in range(1, H):
    r[i]+=r[i-1]

sumj = [l[i]+r[i] for i in range(H)]
print(min(sumj), sumj.count(min(sumj)))


# la=[0]*(H-1)+[l[-1]]
# ra=[r[0]]+[0]*(H-1)
# for i in range(H-2, -1, -1):
#     la[i]=la[i+1]+l[i]
# for i in range(1, H):
#     ra[i]=ra[i-1]+r[i]

# sumj = [la[i]+ra[i] for i in range(H)]
# # sumj = [i+j for i, j in zip(la, ra)]
# print(min(sumj), sumj.count(min(sumj)))