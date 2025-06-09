"""
Accepted
440 [Hard]
Runtime: 1 ms, faster than 34.33% of Python3 online submissions for K-th Smallest in Lexicographical Order.
Memory Usage: 17.66 MB, less than 88.06% of Python3 online submissions for K-th Smallest in Lexicographical Order.
"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countNodes(num):
            res = 0
            nextNei = num + 1
            while num <= n:
                res += min(nextNei, n + 1) - num
                num = num * 10
                nextNei = nextNei * 10
            return res


        curNum, curSteps = 1, 1
        while curSteps < k:
            steps = countNodes(curNum)
            if curSteps + steps <= k:
                curNum += 1
                curSteps += steps
            else:
                curNum = curNum * 10
                curSteps += 1
        return curNum