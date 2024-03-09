"""
Accepted
2540 [Easy]
Runtime: 346 ms, faster than 69.30% of Python3 online submissions for Minimum Common Value.
Memory Usage: 35.57 MB, less than 73.75% of Python3 online submissions for Minimum Common Value.
"""
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left, right = 0, 0
        M, N = len(nums1), len(nums2)
        while left < M and right < N:
            if nums1[left] == nums2[right]:
                return nums1[left]
            if nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return -1