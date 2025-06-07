"""
Accepted
3170 [Medium]
Runtime: 723 ms, faster than 32.38% of Python3 online submissions for Lexicographically Minimum String After Removing Stars.
Memory Usage: 30.04 MB, less than 17.27% of Python3 online submissions for Lexicographically Minimum String After Removing Stars.
"""
class Solution:
    def clearStars(self, s: str) -> str:
        removeIndices = set()
        minHeap = []
        for i, char in enumerate(s):
            if char == '*':
                smallestChar, index = heapq.heappop(minHeap)
                removeIndices.add(-index)
            else:
                heapq.heappush(minHeap, (char, -i))

        res = ""
        for i, char in enumerate(s):
            if char != '*':
                if i in removeIndices:
                    continue
                else:
                    res += char
        return res