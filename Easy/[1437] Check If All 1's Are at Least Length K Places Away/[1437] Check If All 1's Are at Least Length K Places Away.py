"""
Accepted
1437 [Easy]
Runtime: 15 ms, faster than 32.38% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
Memory Usage 21.19 MB, less than 31.85% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
"""
# TC: O(n), SC: O(1)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = k
        for i, bit in enumerate(nums):
            if bit == 0:
                dist += 1
            else:
                if dist < k:
                    return False
                dist = 0
        return True