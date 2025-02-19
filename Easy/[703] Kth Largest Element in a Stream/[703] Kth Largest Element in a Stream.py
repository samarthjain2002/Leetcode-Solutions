"""
Accepted
703 [Easy]
Runtime: 11 ms, faster than 85.82% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 23.55 MB, less than 17.27% of Python3 online submissions for Kth Largest Element in a Stream.
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]       


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)