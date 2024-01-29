"""
Accepted
232 [Easy]
Runtime: 37 ms, faster than 56.95% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 16.50 MB, less than 80.67% of Python3 online submissions for Implement Queue using Stacks.
"""
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.insert(0, x)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()