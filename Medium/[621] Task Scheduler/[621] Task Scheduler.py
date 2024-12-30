"""
Accepted
621 [Medium]
Runtime: 140 ms, faster than 44.46% of Python3 online submissions for Task Scheduler.
Memory Usage:  19.26 MB, less than 12.47% of Python3 online submissions for Task Scheduler.
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = Counter(tasks)
        maxHeap = [-num for num in freqMap.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()

        while maxHeap or queue:
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task < 0:
                    queue.append([task, time + n])
            if queue and queue[0][1] == time:
                task, t = queue.popleft()
                heapq.heappush(maxHeap, task)
            time += 1
        return time



"""
Runtime: 357 ms, faster than 84.27% of Python3 online submissions for Task Scheduler.
Memory Usage:  17.18 MB, less than 59.31% of Python3 online submissions for Task Scheduler.
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        maxElement = max(freq)
        numOfMaxElement = freq.count(maxElement)

        # Calculate the number of intervals required for tasks without the max frequency
        num_intervals = (maxElement - 1) * (n + 1)

        # Add the tasks with the same maximum frequency
        num_intervals += numOfMaxElement

        # Handle the case where there might be idle intervals at the end
        return max(num_intervals, len(tasks))