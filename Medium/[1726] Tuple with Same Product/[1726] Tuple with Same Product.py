"""
Accepted
1726 [Medium]
Runtime: 385 ms, faster than 48.34% of Python3 online submissions for Tuple with Same Product.
Memory Usage: 46.47 MB, less than 41.71% of Python3 online submissions for Tuple with Same Product.
"""
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prodMap = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prodMap[nums[i] * nums[j]] += 1

        res = 0
        for product, count in prodMap.items():
            if count > 1:
                res += ((count * (count - 1)) // 2) * 8
        return res