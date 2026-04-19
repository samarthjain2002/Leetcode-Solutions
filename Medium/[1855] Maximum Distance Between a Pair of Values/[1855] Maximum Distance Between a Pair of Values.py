"""
Accepted
1855 [Medium]
Runtime: 75 ms, faster than 34.71% of Python3 online submissions for Maximum Distance Between a Pair of Values.
Memory Usage: 36.14 MB, less than 21.31% of Python3 online submissions for Maximum Distance Between a Pair of Values.
"""
# Two Pointer Solution
# TC: O(n + m), SC: O(1)
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j = 0
        res = 0
        for i in range(len(nums1)):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                while j < len(nums2) - 1 and nums1[i] <= nums2[j + 1]:
                    j += 1
                res = max(res, j - i)
        return res