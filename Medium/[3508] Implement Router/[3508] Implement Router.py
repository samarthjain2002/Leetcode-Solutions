"""
Accepted
3508 [Medium]
Runtime: 913 ms, faster than 11.86% of Python3 online submissions for Implement Router.
Memory Usage: 91.19 MB, less than 13.91% of Python3 online submissions for Implement Router.
"""
class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packetQueue = deque()
        self.packetSet = set()

        self.destinations = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packetSet:
            return False

        if len(self.packetQueue) == self.memoryLimit:
            popped = self.packetQueue.popleft()
            self.destinations[popped[1]].popleft()
            self.packetSet.remove(popped)
        
        self.packetQueue.append((source, destination, timestamp))
        self.packetSet.add((source, destination, timestamp))
        self.destinations[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if self.packetQueue:
            forward = self.packetQueue.popleft()
            self.packetSet.remove(forward)
            self.destinations[forward[1]].popleft()
            return list(forward)
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = len(self.destinations[destination])
        low, high = 0, len(self.destinations[destination]) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if self.destinations[destination][mid] >= startTime:
                left = mid
                high = mid - 1
            else:
                low = mid + 1

        right = -1
        low, high = 0, len(self.destinations[destination]) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if self.destinations[destination][mid] <= endTime:
                right = mid
                low = mid + 1
            else:
                high = mid - 1

        if left <= right:
            return right - left + 1
        else:
            return 0



# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)