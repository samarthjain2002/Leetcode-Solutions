"""
Accepted
1189 [Easy]
Runtime: 3 ms, faster than 61.87% of Python3 online submissions for Maximum Number of Balloons.
Memory Usage: 19.41 MB, less than 9.97% of Python3 online submissions for Maximum Number of Balloons.
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)

        res = inf
        for char in "balon":
            if char in "ban":
                res = min(res, freq[char])
            elif char in "lo":
                res = min(res, freq[char] // 2)
        return res if res < inf else 0