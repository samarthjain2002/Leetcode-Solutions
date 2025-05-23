"""
Accepted
473 [Medium]
Runtime: 3799 ms, faster than 36.33% of Python3 online submissions for Matchsticks to Square.
Memory Usage: 17.74 MB, less than 85.70% of Python3 online submissions for Matchsticks to Square.
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        sideLength = total // 4
        matchsticks.sort(reverse=True)

        sides = [0] * 4
        def backtrack(msIndex):
            if msIndex == len(matchsticks):
                return True

            for i in range(4):
                if sides[i] + matchsticks[msIndex] <= sideLength:
                    sides[i] += matchsticks[msIndex]
                    if backtrack(msIndex + 1):
                        return True
                    sides[i] -= matchsticks[msIndex]
            return False
            
        
        return backtrack(0)