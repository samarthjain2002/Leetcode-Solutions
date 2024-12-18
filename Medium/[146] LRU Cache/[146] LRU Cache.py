"""
Accepted
146 [Medium]
Runtime: 124 ms, faster than 75.17% of Python3 online submissions for LRU Cache.
Memory Usage:  78.30 MB, less than 15.34% of Python3 online submissions for LRU Cache.
"""
class ListNode:
    def __init__(self, key, val, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.ptr = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # If the most-recently used key is fetched again
        if self.ptr.key == key:
            return self.ptr.val

        # If the fetched node has a left node
        if self.cache[key].left:
            self.cache[key].left.right = self.cache[key].right
        self.cache[key].right.left = self.cache[key].left

        # Pointer points to the fetched node
        self.ptr.right = self.cache[key]
        self.cache[key].left = self.ptr
        # Pointer becomes the fetched node
        self.ptr = self.cache[key]

        return self.ptr.val

    def put(self, key: int, value: int) -> None:
        # If there is no node/cache is empty
        if not self.ptr:
            newNode = ListNode(key, value)
            self.cache[key] = newNode
            self.ptr = newNode
            self.capacity -= 1
        # If the key is in the cache
        elif key in self.cache:
            self.cache[key].val = value
            # Moving the node to the right-most position is written in the get method
            self.get(key)
        # If there is space in the cache
        elif self.capacity:
            newNode = ListNode(key, value, self.ptr)
            self.cache[key] = newNode
            self.ptr.right = newNode
            self.ptr = newNode
            self.capacity -= 1
        # If the capacity of the cache is exhausted
        else:
            # Cur pointer moves to the left-most node
            cur = self.ptr
            while cur.left:
                cur = cur.left
            # Left-most node is remvoed from the cache
            del self.cache[cur.key]
            
            # If there are more than 1 nodes
            if cur.right:
                cur.right.left = None
            # If there is only 1 node
            else:
                self.ptr = None

            # Adding the the key-value pair to the right-most end
            self.capacity += 1
            self.put(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)