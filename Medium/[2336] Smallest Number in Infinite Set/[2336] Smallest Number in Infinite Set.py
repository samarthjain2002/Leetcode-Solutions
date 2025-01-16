"""
Accepted
2336 [Medium]
Runtime: 28 ms, faster than 42.33% of Python3 online submissions for Smallest Number in Infinite Set.
Memory Usage: 18.50 MB, less than 28.45% of Python3 online submissions for Smallest Number in Infinite Set.
"""
class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = [i for i in range(1, 1001)]
        heapq.heapify(self.minHeap)
        self.hashSet = set([i for i in range(1, 1001)])  

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.minHeap)
        self.hashSet.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.hashSet:
            self.hashSet.add(num)
            heapq.heappush(self.minHeap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)