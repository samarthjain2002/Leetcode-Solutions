"""
Accepted
416 [Medium]
Runtime: 156 ms, faster than 95.94% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage:  18.86 MB, less than 59.34% of Python3 online submissions for Partition Equal Subset Sum.
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set([0])
        for num in nums:
            nextDP = dp.copy()
            for t in dp:
                if t + num == target:
                    return True
                nextDP.add(t + num)
            dp = nextDP
        return target in dp