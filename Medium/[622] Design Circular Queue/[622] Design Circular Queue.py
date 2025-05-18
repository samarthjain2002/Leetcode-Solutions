"""
Accepted
622 [Medium]
Runtime: 4 ms, faster than 80.52% of Python3 online submissions for Design Circular Queue.
Memory Usage: 18.44 MB, less than 74.68% of Python3 online submissions for Design Circular Queue.
"""
class ListNode:
    def __init__(self, val, nxt = None):
        self.val = val
        self.nxt = nxt


class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.curSize = 0
        # Front is a dummy node (True front node is next to this dummy node)
        self.front = ListNode(-1)
        self.rear = self.front

    def enQueue(self, value: int) -> bool:
        # EnQueue operation at rear
        if self.curSize == self.k:
            return False

        self.rear.nxt = ListNode(value)
        self.rear = self.rear.nxt
        self.curSize += 1
        
        return True

    def deQueue(self) -> bool:
        # DeQueue operation at front
        if self.curSize == 0:
            return False

        # The next node becomes the dummy front node
        self.front = self.front.nxt
        self.curSize -= 1
        
        return True        

    def Front(self) -> int:
        if self.curSize == 0:
            return -1

        return self.front.nxt.val

    def Rear(self) -> int:
        if self.curSize == 0:
            return -1

        return self.rear.val

    def isEmpty(self) -> bool:
        return self.curSize == 0

    def isFull(self) -> bool:
        return self.curSize == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()