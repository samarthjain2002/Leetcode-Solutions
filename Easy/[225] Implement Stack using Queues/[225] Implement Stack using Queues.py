"""
Accepted
225 [Easy]
Runtime: 39 ms, faster than 41.22% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 16.51 MB, less than 68.63% of Python3 online submissions for Implement Stack using Queues.
"""
class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()