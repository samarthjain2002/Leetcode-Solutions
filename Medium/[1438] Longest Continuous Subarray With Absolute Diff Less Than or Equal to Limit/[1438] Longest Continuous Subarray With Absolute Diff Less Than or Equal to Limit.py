"""
Accepted
1438 [Easy]
Runtime: 458 ms, faster than 50.32% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
Memory Usage: 26.04 MB, less than 69.37% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        maxSize = 0
        minQueue = collections.deque()
        maxQueue = collections.deque()
        for right in range(len(nums)):
            while minQueue and nums[minQueue[-1]] >= nums[right]:
                minQueue.pop()
            minQueue.append(right)

            while maxQueue and nums[maxQueue[-1]] <= nums[right]:
                maxQueue.pop()
            maxQueue.append(right)

            while minQueue and maxQueue and nums[maxQueue[0]] - nums[minQueue[0]] > limit:
                left += 1
                
                if minQueue[0] < left:
                    minQueue.popleft()
                if maxQueue[0] < left:
                    maxQueue.popleft()

                size = 0
            maxSize = max(maxSize, right - left + 1)
        return maxSize