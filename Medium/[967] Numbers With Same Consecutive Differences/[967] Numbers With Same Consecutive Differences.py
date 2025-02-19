"""
Accepted
967 [Medium]
Runtime: 7 ms, faster than 46.06% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 18.24 MB, less than 28.75% of Python3 online submissions for Numbers With Same Consecutive Differences.
"""
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        numbers = []
        
        def backtrack(string):
            if len(string) == n:
                numbers.append(int(string))
                return
            
            if not string:
                for i in range(1, 10):
                    if i + k < 10 or i - k >= 0:
                        backtrack(string + str(i))
            else:
                if int(string[-1]) + k < 10:
                    backtrack(string + str(int(string[-1]) + k))
                if k != 0 and int(string[-1]) - k >= 0:
                    backtrack(string + str(int(string[-1]) - k))

        backtrack("")
        return numbers