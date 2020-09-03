def net_el_list(idx, li, done, computers):
    # 컴터의 idx를 넣으면, 해당 컴 포함, 연결된 모든 컴들의 idx들의 리스트를 반환.
    adj_list = [idx2 for idx2, i in enumerate(computers[idx]) if i==1]
    li = list(set(li)|set(adj_list))
    # li.remove(idx)
    done.append(idx)
    li = list(set(li)-set(done))
    if len(li)>0:
        done = net_el_list(li[0], li, done, computers)    
    return done

def solution(n, computers):    
    tot = list(range(n)) # 전체 컴터들의 리스트. ex: [0,1,2,..]
    num_net = 0    
    while len(tot)>0:
        li = []; done = [] 
        print('li:{}, done:{}'.format(li, done))
        el_list = net_el_list(tot[0], li, done, computers)
        print('el_list:',el_list)
        tot = list(set(tot)-set(el_list))
        print('tot:',tot)
        num_net+=1
        print('---------------')
    return num_net

n_ex = 3; computers_ex = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
ret = solution(n_ex, computers_ex)
print(ret)
