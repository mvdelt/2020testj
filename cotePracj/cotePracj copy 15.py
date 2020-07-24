def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    
    def maketree(root):
        childtree = {root:{}}
        for branch in words:
            if branch == root:
                continue
            for idx in range(len(branch)):
                if branch[:idx]+branch[idx+1:] == root[:idx]+root[idx+1:]:
                    childtree[root].update({branch:{}})
                    break
        return childtree

    
    def recur(childtree, count):
        count+=1
        if count >=51:
            return childtree
        for root in childtree:
            childtree = maketree(root)
            recur(childtree, count)
    
    childtree = maketree(target)
    childtree = recur(childtree, 0)
    return childtree
    


ret = solution('hit','cog',["hot", "dot", "dog", "lot", "log", "cog"])
print(ret)