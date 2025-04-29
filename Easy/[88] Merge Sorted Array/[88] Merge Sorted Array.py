"""
Accepted
88 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 17.82 MB, less than 43.94% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = len(nums1) - 1
        while m - 1 >= 0 and n - 1 >= 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[pos] = nums1[m - 1]
                m -= 1
            else:
                nums1[pos] = nums2[n - 1]
                n -= 1
            pos -= 1
        while m - 1 >= 0:
            nums1[pos] = nums1[m - 1]
            m -= 1
            pos -= 1
        while n - 1 >= 0:
            nums1[pos] = nums2[n - 1]
            n -= 1
            pos -= 1