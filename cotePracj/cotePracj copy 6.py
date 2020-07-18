def solution(clothes):
    
    c_dict = {}
    for c in clothes:
        print(c_dict)
        c_dict.setdefault(c[1],[]).append(c[0])
    
    prod = 1
    for v in c_dict.values():
        prod *= len(v)+1
        
    return (prod-1)

c_ex1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(c_ex1))