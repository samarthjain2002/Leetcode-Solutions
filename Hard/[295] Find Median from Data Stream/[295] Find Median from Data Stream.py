"""
Accepted
295 [Hard]
Runtime: 108 ms, faster than 90.53% of Python3 online submissions for Find Median from Data Stream.
Memory Usage:  39.62 MB, less than 24.22% of Python3 online submissions for Find Median from Data Stream.
"""
class MedianFinder:

    def __init__(self):
        # small is a maxHeap, large is a minHeap
        self.small, self.large = [], []
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # If small has a value greater than smallest value of large
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # If length of small and large is uneven (> 2 or < 2)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()