"""
Accepted
1207 [Easy]
Runtime: 43 ms, faster than 62.10% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 17.45 MB, less than 25.02% of Python3 online submissions for Unique Number of Occurrences.
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = defaultdict(int)
        for i in arr:
            occ[i] += 1

        uniq = set()
        for val in occ.values():
            if val in uniq:
                return False
            else:
                uniq.add(val)

        return True