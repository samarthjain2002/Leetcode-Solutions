"""
Accepted
933 [Easy]
Runtime: 186 ms, faster than 88.83% of Python3 online submissions for Number of Recent Calls.
Memory Usage:  22.12 MB, less than 30.83% of Python3 online submissions for Number of Recent Calls.
"""
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)