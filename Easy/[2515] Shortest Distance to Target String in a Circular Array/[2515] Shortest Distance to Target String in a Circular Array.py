"""
Accepted
2515 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Shortest Distance to Target String in a Circular Array.
Memory Usage: 19.40 MB, less than 20.97% of Python3 online submissions for Shortest Distance to Target String in a Circular Array.
"""
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        for i in range(len(words)):
            if words[startIndex - i] == target:
                return i
            if words[(startIndex + i) % len(words)] == target:
                return i
        return -1