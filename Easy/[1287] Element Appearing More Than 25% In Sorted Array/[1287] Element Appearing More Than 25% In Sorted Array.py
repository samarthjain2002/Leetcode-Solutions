"""
Accepted
1287 [Easy]
Runtime: 97 ms, faster than 39.02% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
Memory Usage: 17.46 MB, less than 95.95% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 1
        res = arr[0]
        for i in arr[1:]:
            if count > (1 * len(arr) / 4):
                return res
            if i == res:
                count += 1
            else:
                res = i
                count = 1
        return res