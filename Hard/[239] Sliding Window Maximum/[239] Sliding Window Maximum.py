"""
Accepted
239 [Hard]
Runtime: 1056 ms, faster than 95.20% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 32.16 MB, less than 83.29% of Python3 online submissions for Sliding Window Maximum.
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        res = []
        queue = collections.deque()
        
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])

        for i in range(k, N):
            while queue and queue[0] <= i - k:
                queue.popleft()

            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        
        return res