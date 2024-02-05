"""
Accepted
387 [Easy]
Runtime: 79 ms, faster than 83.15% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 16.71 MB, less than 66.48% of Python3 online submissions for First Unique Character in a String.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniques = []
        detected = set()
        for char in s:
            if char not in detected:
                uniques.append(char)
            elif char in uniques:
                del uniques[uniques.index(char)]
            detected.add(char)

        if uniques:
            return s.index(uniques[0])
        else:
            return -1