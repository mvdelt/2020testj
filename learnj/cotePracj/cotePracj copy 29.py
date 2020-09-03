class Truck:
    def __init__(self, w, loc=1):
        self.loc = loc
        self.w = w

def solution(bridge_length, weight, truck_weights):
     
    num_trucks = len(truck_weights)
    
    # i. Truck 옵젝들의 리스트.
    trucks = [Truck(w) for w in truck_weights]        
        
    sec = 0
    bridge=[]
    fin=[]
    while not len(fin)==num_trucks:
        sec+=1        
        for ontruck in bridge[:]: # i. 또 전에자주햇던 실수 반복햇다!!!ㅡㅡ;; 그냥 bridge라고 한뒤에 bridge.pop해버리면 for문이 이상하게돌자나!!! bridge를 카피해준놈을 쓰든지해야지 bridge[:] 이런식으로.
            ontruck.loc+=1
            if ontruck.loc > bridge_length:
                fin.append(bridge.pop(0))

        if len(trucks)>0:
            if sum([ontruck.w for ontruck in bridge]) + trucks[0].w  <= weight:
                bridge.append(trucks.pop(0))

        print(f'sec:{sec}, fin:{[(truck.w, truck.loc) for truck in fin]}, br:{[(truck.w, truck.loc) for truck in bridge]}, trucks:{[truck.w for truck in trucks]}, numtr:{num_trucks}')
    return sec

br_len, weight, tr_ws = 2, 10, [7, 4, 5, 6]
ret = solution(br_len, weight, tr_ws)
print(ret)