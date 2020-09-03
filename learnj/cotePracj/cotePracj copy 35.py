class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        1. s에서 원소 하나씩 돌면서, set에 이미 있나 쳌, 없으면 넣음.
        2. set에 A이미 있으면(A'), set의 원소갯수를 hubo 에 기록하고,
            s에서 지난번 컷햇던것이후부터 A'까지의 원소들을, set에서 뺌.
            어디까지 컷햇나 저장.
            set에 A를 넣음.
            다음원소부터 1.로돌아가서 다시 쳌 시작.
        3. 다돌앗으면,
            set의 길이를 hubo 에 넣음(2.가 실행되지않앗을경우 대비). 
            hubo중에서 젤 큰 숫자 리턴.          
        """
        setj = set()
        hubo = set()
        idxstack = []
        for idx, i in enumerate(s):
            if i not in setj:
                setj.add(i)
            else:
                hubo.add(len(setj))

                findx = idx-1
                while not s[findx]==i:
                    findx-=1
                recentSame_idx = findx

                if len(idxstack)==0:            
                    setj -= set(s[:recentSame_idx+1])
                else:
                    setj -= set(s[idxstack[-1]+1:recentSame_idx+1])
                idxstack.append(recentSame_idx)
                setj.add(i)
        hubo.add(len(setj))

        return max(hubo)
                

sol = Solution()
s = "aabaab!bb"
ret = sol.lengthOfLongestSubstring(s)
print(ret)          