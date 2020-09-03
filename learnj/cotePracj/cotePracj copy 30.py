# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def makeAPI(n, firstBV):
    if n<firstBV:
        print('j) firstBV should not be bigger than n.')
    li1 = [0 for i in range(1, firstBV)]
    li2 = [1 for i in range(firstBV, n+1)]
    verList = li1+li2
    def isBadVersion(i):
        if verList[i-1]==0:
            return False
        else:
            return True
    return isBadVersion

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        pos = int(n/2)
        while ~~:
            if isBadVersion(pos):
                delt = abs(oldpos-pos)
                pos = pos-delt
                delt = 
            else:
                pos = pos + int(pos/2)

        # pos = int(n/2)
        # delta = int(n/2)
        # while True:
        #     delta=int(delta/2)
        #     if isBadVersion(pos):
        #         pos -= int(delta)
        #         if delta<=1:
        #             if not isBadVersion(pos):
        #                 return pos+1
        #             else:
        #                 return pos
        #     else:
        #         pos += int(delta)
        #         if delta<=1:
        #             if isBadVersion(pos):
        #                 return pos
        #             else:
        #                 return pos+1

n_ex = 20
firBV_ex = 10
isBadVersion = makeAPI(n_ex, firBV_ex)
# print([isBadVersion(i) for i in range(1,n_ex+1)]) # i. 만들어준 API(isBadVersion함수)잘되나 테스트. 원하는대로 잘 작동.

solution=Solution()
ret = solution.firstBadVersion(n_ex)
print('first bad version:', ret)
