"""
Accepted
777 [Easy]
Runtime: 8 ms, faster than 63.01% of Python3 online submissions for Swap Adjacent in LR String.
Memory Usage: 17.37 MB, less than 21.79% of Python3 online submissions for Swap Adjacent in LR String.
"""
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        M , N = len(start), len(result)
        left = 0
        for right in range(N):
            if result[right] == 'X':
                continue
            
            while left < M and start[left] == 'X':
                left += 1

            if left == M or start[left] != result[right]:
                return False
            
            if start[left] == 'L' and left < right:
                return False
            if start[left] == 'R' and left > right:
                return False

            left += 1

        while left < M:
            if start[left] != 'X':
                return False
            left += 1

        return True