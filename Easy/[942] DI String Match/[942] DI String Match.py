"""
Accepted
942 [Easy]
Runtime: 6 ms, faster than 16.78% of Python3 online submissions for DI String Match.
Memory Usage: 18.92 MB, less than 15.27% of Python3 online submissions for DI String Match.
"""
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        low, high = 0, len(s)

        for i in range(len(s)):
            if s[i] == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        res.append(low)

        return res