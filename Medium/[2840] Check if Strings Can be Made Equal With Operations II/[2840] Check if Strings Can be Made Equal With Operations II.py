"""
Accepted
2840 [Medium]
Runtime: 51 ms, faster than 83.58% of Python3 online submissions for Check if Strings Can be Made Equal With Operations II.
Memory Usage: 20.00 MB, less than 82.09% of Python3 online submissions for Check if Strings Can be Made Equal With Operations II.
"""
# HashMap Approach
# TC: O(n), SC: O(n)
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])



"""
Runtime: 244 ms, faster than 6.72% of Python3 online submissions for Check if Strings Can be Made Equal With Operations II.
Memory Usage: 22.72 MB, less than 6.72% of Python3 online submissions for Check if Strings Can be Made Equal With Operations II.
"""
# Sorting Approach
# TC: O(nlogn), SC: O(n)
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd1 = [char for i, char in enumerate(s1) if i % 2 == 1]
        even1 = [char for i, char in enumerate(s1) if i % 2 == 0]
        odd2 = [char for i, char in enumerate(s2) if i % 2 == 1]
        even2 = [char for i, char in enumerate(s2) if i % 2 == 0]

        return sorted(odd1) == sorted(odd2) and sorted(even1) == sorted(even2)