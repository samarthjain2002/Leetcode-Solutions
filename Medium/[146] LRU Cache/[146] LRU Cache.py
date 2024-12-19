"""
Accepted
146 [Medium]
Runtime: 124 ms, faster than 75.18% of Python3 online submissions for LRU Cache.
Memory Usage:  78.30 MB, less than 15.44% of Python3 online submissions for LRU Cache.
"""
class ListNode:
    def __init__(self, key, val, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1, self.head)
        self.head.right = self.tail

    def remove_node(self, node):
        prev, nxt = node.left, node.right
        prev.right, nxt.left = node.right, node.left

    def add_node(self, node):
        prev, nxt = self.tail.left, self.tail
        prev.right = nxt.left = node
        node.left, node.right = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove_node(self.cache[key])
        self.add_node(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove_node(self.cache[key])
            self.add_node(self.cache[key])
            return
        elif len(self.cache) == self.capacity:
            lru = self.head.right
            self.remove_node(lru)
            del self.cache[lru.key]
        newNode = ListNode(key, value)
        self.add_node(newNode)
        self.cache[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)