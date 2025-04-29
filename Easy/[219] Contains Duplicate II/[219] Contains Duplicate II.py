"""
Accepted
219 [Easy]
Runtime: 442 ms, faster than 94.95% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 29.70 MB, less than 64.68% of Python3 online submissions for Contains Duplicate II.
"""
# Hash Table Solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i, n in enumerate(nums):
            if n in d and abs(i - d[n]) <= k:
                return True
            else:
                d[n] = i
        
        return False



"""
Runtime: 90 ms, faster than 6.63% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 34.47 MB, less than 36.51% of Python3 online submissions for Contains Duplicate II.
"""
# Sliding Window Solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        numFreq = Counter(nums[ : min(len(nums), k + 1)])
        for freq in numFreq.values():
            if freq >= 2:
                return True

        if k + 1 >= len(nums):
            return False

        for i in range(k + 1, len(nums)):
            numFreq[nums[i]] += 1
            numFreq[nums[i - k - 1]] -= 1

            if numFreq[nums[i]] == 2:
                return True

        return False