"""
Accepted
2918 [Medium]
Runtime: 841 ms, faster than 76.38% of Python3 online submissions for Minimum Equal Sum of Two Arrays After Replacing Zeros.
Memory Usage: 34.69 MB, less than 91.29% of Python3 online submissions for Minimum Equal Sum of Two Arrays After Replacing Zeros.
"""
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        zero1 = nums1.count(0)
        sum1 += zero1
        
        sum2 = sum(nums2)
        zero2 = nums2.count(0)
        sum2 += zero2

        if sum1 < sum2 and zero1 == 0:
            return -1
        elif sum2 < sum1 and zero2 == 0:
            return -1
        else:
            return max(sum1, sum2)