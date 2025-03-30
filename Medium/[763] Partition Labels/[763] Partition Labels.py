"""
Accepted
763 [Medium]
Runtime: 2 ms, faster than 94.58% of Python3 online submissions for Partition Labels.
Memory Usage: 17.64 MB, less than 85.21% of Python3 online submissions for Partition Labels.
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, char in enumerate(s):
            lastIndex[char] = i

        res = []
        first = 0
        while first < len(s):
            left, right = first, lastIndex[s[first]]
            while left < right:
                if lastIndex[s[left]] > right:
                    right = lastIndex[s[left]]
                left += 1

            res.append(right - first + 1)
            first = right + 1
            
        return res