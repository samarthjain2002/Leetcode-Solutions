"""
Accepted
1094 [Medium]
Runtime: 4 ms, faster than 34.08% of Python3 online submissions for Car Pooling.
Memory Usage: 18.15 MB, less than 74.79% of Python3 online submissions for Car Pooling.
"""
# Min-heap approach
# TC: O(nlog(n)), SC: O(n)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort based on starting times
        trips.sort(key = lambda trip: trip[1])

        curPassengers = 0
        minHeap = []
        for i in range(len(trips)):
            while minHeap and minHeap[0][0] <= trips[i][1]:
                endTime, numPassengers = heapq.heappop(minHeap)
                curPassengers -= numPassengers

            # If we cannot onload passenger more than the capacity
            if curPassengers + trips[i][0] > capacity:
                return False

            # Onload the passengers
            curPassengers += trips[i][0]
            heapq.heappush(minHeap, (trips[i][2], trips[i][0]))

        return True