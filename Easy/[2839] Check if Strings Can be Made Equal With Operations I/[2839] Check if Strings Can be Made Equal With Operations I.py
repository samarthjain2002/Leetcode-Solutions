"""
Accepted
2839 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Check if Strings Can be Made Equal With Operations I.
Memory Usage: 19.24 MB, less than 73.74% of Python3 online submissions for Check if Strings Can be Made Equal With Operations I.
"""
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (
            ((s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0]))
            and
            ((s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1]))
        )



"""
Runtime: 4 ms, faster than 7.82% of Python3 online submissions for Check if Strings Can be Made Equal With Operations I.
Memory Usage: 19.33 MB, less than 41.34% of Python3 online submissions for Check if Strings Can be Made Equal With Operations I.
"""
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])