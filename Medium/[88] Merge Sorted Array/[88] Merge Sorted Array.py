"""
Accepted
88 [Medium]
Runtime: 41 ms, faster than 47.70% of Python3 online submissions for Merge Sorted Array.
Memory Usage:  16.56 MB, less than 72.83% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else:
                nums1[last] = nums1[m - 1]
                m -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            last, n = last - 1, n - 1