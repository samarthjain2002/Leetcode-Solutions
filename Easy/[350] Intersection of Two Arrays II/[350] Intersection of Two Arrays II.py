"""
Accepted
350 [Easy]
Runtime: 92 ms, faster than 5.25% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 16.80 MB, less than 31.35% of Python3 online submissions for Intersection of Two Arrays II.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Dict = {num:nums1.count(num) for num in nums1}
        nums2Dict = {num:nums2.count(num) for num in nums2}
        res = []
        for key in nums1Dict.keys():
            if key in nums2Dict:
                minimum = min(nums1Dict[key], nums2Dict[key])
                for _ in range(minimum):
                    res.append(key)

        return res