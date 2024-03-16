"""
Accepted
525 [Medium]
Runtime: 641 ms, faster than 19.61% of Python3 online submissions for Contiguous Array.
Memory Usage:  22.47 MB, less than 15.74% of Python3 online submissions for Contiguous Array.
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        count = 0
        for i in range(N):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            nums[i] = count
        nums.insert(0, 0)
        
        hashMap = defaultdict(int)
        res = 0
        for i in range(N + 1):
            hashMap[nums[i]] = i

        for i in range(N + 1):
            res = max(res, hashMap[nums[i]] - i)

        return res