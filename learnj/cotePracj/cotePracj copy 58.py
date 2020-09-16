"""
LeetCode 'Word Ladder' 문제. 프로그래머스에서 봤던 문제임.
2020.09.16.수욜아침. 08:06~
"""

from typing import List

class Solution:

    # def __init__(self):
    #     self.minLen = float('inf')
    #     self.minLi = []

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        self.memo={}
        self.endWord = endWord

        # endWord 가 wordList 에 없으면 불가.
        if endWord not in wordList:
            return 0
        
        ans = self.minlen(beginWord, wordList)
        if ans == float('inf'):
            return 0
        return ans

    def minlen(self, beginWord, wordList):

        if (beginWord, *wordList) in self.memo:
            return self.memo[(beginWord, *wordList)]

        nextLi=[]
        for word in wordList:
            numDiff = sum(1 if a!=b else 0 for a,b in zip(beginWord, word))
            if numDiff==1:
                nextLi+=[word]

        counts=[float('inf')] # len(nextLi)==0 이면 inf 리턴되도록 미리 inf 넣어줌.
        for nextword in nextLi:
            if nextword == self.endWord:                                
                return 2
            newLi = wordList.copy()
            newLi.remove(nextword)
            counts+=[self.minlen(nextword, newLi)]
        
        self.memo[(beginWord, *wordList)] = min(counts)+1
        
        return min(counts)+1


bword='hit'
eword='cog'
wLi = ["hot","dot","dog","lot","log","cog"]
wLi =  ["hot","dot","dog","lot","log"]
wLi = ["hot","dot","dol","lot","log","com", 'gol', 'cog']
sol=Solution()
ret = sol.ladderLength(bword, eword, wLi)
print(ret)