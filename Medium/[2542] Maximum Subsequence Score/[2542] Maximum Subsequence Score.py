"""
Accepted
2542 [Medium]
Runtime: 254 ms, faster than 11.07% of Python3 online submissions for Maximum Subsequence Score.
Memory Usage: 41.34 MB, less than 36.76% of Python3 online submissions for Maximum Subsequence Score.
"""
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = [[nums2[i], nums1[i]] for i in range(len(nums1))]
        nums.sort(reverse = True)

        minHeap = []
        heapq.heapify(minHeap)
        res = 0
        totalSum = 0
        for i in range(len(nums)):
            if i + 1 < k:
                heapq.heappush(minHeap, nums[i][1])
                totalSum += nums[i][1]
            elif i + 1 == k:
                heapq.heappush(minHeap, nums[i][1])
                totalSum += nums[i][1]
                res = max(res, totalSum * nums[i][0])
            else:
                totalSum -= heapq.heappop(minHeap)
                totalSum += nums[i][1]
                heapq.heappush(minHeap, nums[i][1])
                res = max(res, totalSum * nums[i][0])
        return res