"""
Accepted
229 [Medium]
Runtime: 105 ms, faster than 40.54% of Python3 online submissions for Majority Element II.
Memory Usage:  17.94 MB, less than 62.13% of Python3 online submissions for Majority Element II.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        hashMap = defaultdict(int)
        majority = []
        for i in range(N):
            hashMap[nums[i]] += 1
            if hashMap[nums[i]] > N / 3 and nums[i] not in majority:
                majority.append(nums[i])

        return majority
    

"""
Accepted
229 [Medium]
Runtime: 92 ms, faster than 91.81% of Python3 online submissions for Majority Element II.
Memory Usage:  17.89 MB, less than 81.52% of Python3 online submissions for Majority Element II.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) / 3
        return [n for n, c in Counter(nums).items() if c > threshold]