# i. 2020.08.01. 전에 함 봣다가 생각으로 설계는 햇는데 못풀엇다가, 오늘 다시 한시간넘게붙잡고 겨우해결..;;
# 내 방식은, 따지자면 BFS 방식이 될거임 아마.
# 가장 짧은 단계를 찾아야 하므로, DFS로 깊게들어가버리는건 의미가 없음. 일단 한 층에서 다 검색하고, 없으면 다음층으로 들어가는 식으로 햇음.

# ㅇ)
# 1. layer 찾고, 합집합에 합치고,
# 2. 위의 layer 에서 target 잇으면 1반환, 없으면 0반환.

# layer의 각 단어마다 ㅇ) 수행하여 그 합집합을 새로운 layer로. 모든단어다돌앗으면 count++.

def solution(begin, target, words):   

    layer_count=0
    sumlayer=set()

    def finder(a):
        nonlocal sumlayer
        layer = [word for word in words if 1==numUnmatchChar(a, word)]
        sumlayer|=set(layer)
        # breakpoint()

        if target in set(layer): return 1
        else: return 0

    def sol(layer):
        nonlocal layer_count, sumlayer
        layer_count+=1
        sumlayer = set()
        for lay in layer:
            if finder(lay)==1: return layer_count
        layer=sumlayer
        # breakpoint()
        return sol(layer)


    def numUnmatchChar(word1, word2):
        unmat_count = 0
        for idx, char in enumerate(word1):
            if char != word2[idx]:
                unmat_count+=1
        return unmat_count

    # nth_layer = 0

    # def inner(layer):
    #     global nth_layer
        
    #     if target not in set(words): return 0      
        
    #     for lay in layer:    
    #         next_layer = [word for word in words if 1==numUnmatchChar(lay, word)]
    #         nth_layer++
    #         if target in set(next_layer):
    #             return nth_layer
    #     inner(layer)
        
    
    if target not in set(words): return 0
    return sol([begin])

begin_ex = "hit"
target_ex = "cog"
words_ex = ["hot", "dot", "dog", "lot", "log", "cog"] # i. should be 4

print(solution(begin_ex, target_ex, words_ex))