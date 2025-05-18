"""
Accepted
1834 [Medium]
Runtime: 467 ms, faster than 15.81% of Python3 online submissions for Single-Threaded CPU.
Memory Usage: 59.92 MB, less than 38.27% of Python3 online submissions for Single-Threaded CPU.
"""
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # enqueueTime, processingTime, index
        tasks = sorted([[task[0], task[1], index] for index, task in enumerate(tasks)])
        
        minHeap = []
        res = []
        curTime = 0
        ptr = 0
        while len(res) < len(tasks):
            while ptr < len(tasks) and tasks[ptr][0] <= curTime:
                heapq.heappush(minHeap, (tasks[ptr][1], tasks[ptr][2]))
                ptr += 1

            if not minHeap:
                curTime = tasks[ptr][0]
            else:
                processingTime, index = heapq.heappop(minHeap)
                res.append(index)
                curTime += processingTime

        return res