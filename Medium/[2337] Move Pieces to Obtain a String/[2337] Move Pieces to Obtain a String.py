"""
Accepted
2337 [Easy]
Runtime: 102 ms, faster than 87.10% of Python3 online submissions for Move Pieces to Obtain a String.
Memory Usage: 17.77 MB, less than 39.52% of Python3 online submissions for Move Pieces to Obtain a String.
"""
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        M , N = len(start), len(target)
        left = 0
        for right in range(N):
            if target[right] == '_':
                continue
            
            while left < M and start[left] == '_':
                left += 1

            if left == M or start[left] != target[right]:
                return False
            
            if start[left] == 'L' and left < right:
                return False
            if start[left] == 'R' and left > right:
                return False

            left += 1

        while left < M:
            if start[left] != '_':
                return False
            left += 1

        return True