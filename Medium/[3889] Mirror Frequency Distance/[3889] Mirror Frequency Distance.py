"""
Accepted
3889 [Medium]
Runtime: 443 ms, faster than 40.00% of Python3 online submissions for Mirror Frequency Distance.
Memory Usage: 23.83 MB less than 40.78% of Python3 online submissions for Mirror Frequency Distance.
"""
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = Counter(s)
        vis = set()
        res = 0
        for c in s:
            if c in vis:
                continue
                
            vis.add(c)
            if c in "0123456789":
                m = str(abs(int(c) - 9))
            else:
                m = chr(abs(ord(c) - ord('z')) + ord('a'))
            vis.add(m)

            res += abs(freq[c] - freq[m])
        return res