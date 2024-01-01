"""
Accepted
455 [Easy]
Runtime: 320 ms, faster than 8.48% of Python3 online submissions for Assign Cookies
Memory Usage: 19.26 MB, less than 8.91% of Python3 online submissions for Assign Cookies
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        contentChildren = 0
        left, right = 0, 0
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                contentChildren += 1
                left += 1
                right += 1
            else:
                right += 1
        return contentChildren