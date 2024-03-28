"""
Accepted
2958 [Medium]
Runtime: 1162 ms, faster than 51.12% of Python3 online submissions for Length of Longest Subarray With at Most K Frequency.
Memory Usage: 31.05 MB, less than 74.68% of Python3 online submissions for Length of Longest Subarray With at Most K Frequency.
"""
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        N = len(nums)
        left = 0
        hashMap = defaultdict(int)
        for right in range(N):
            while hashMap[nums[right]] == k:
                hashMap[nums[left]] -= 1
                left += 1
            hashMap[nums[right]] += 1
            res = max(res, right - left + 1)
        return res