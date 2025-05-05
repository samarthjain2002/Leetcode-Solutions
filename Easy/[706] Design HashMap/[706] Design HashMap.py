"""
Accepted
706 [Easy]
Runtime: 69 ms, faster than 25.93% of Python3 online submissions for Design HashSet.
Memory Usage: 21.13 MB, less than 34.10% of Python3 online submissions for Design HashSet.
"""
# Binary Search Tree Approach
# TC: O(log(n)), SC: O(n)
class BSTNode:
    def __init__(self, key, val = None, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.key}, {self.val}, {self.nxt}"


class MyHashMap:
    def __init__(self):
        self.root = BSTNode(-1, -1)

    def put(self, key: int, value: int) -> None:
        ptr = self.root
        while True:
            if key < ptr.key and ptr.left:
                ptr = ptr.left
            elif key > ptr.key and ptr.right:
                ptr = ptr.right
            elif key == ptr.key:
                ptr.val = value
                return
            else:
                break

        if key < ptr.key:
            ptr.left = BSTNode(key, value)
        elif key > ptr.key:
            ptr.right = BSTNode(key, value)

    def get(self, key: int) -> int:
        ptr = self.root
        while ptr:
            if ptr.key == key:
                return ptr.val
            elif key < ptr.key:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return -1

    def remove(self, key: int) -> None:
        ptr = self.root
        while ptr and ptr.key != key:
            if ptr.left and ptr.left.key == key:
                # If ptr.left has no children
                if not ptr.left.left and not ptr.left.right:
                    ptr.left = None
                    return
                # If ptr.left has 1 child
                elif (not ptr.left.left and ptr.left.right) or (ptr.left.left and not ptr.left.right):
                    ptr.left = ptr.left.left or ptr.left.right
                    return
            elif ptr.right and ptr.right.key == key:
                # If ptr.right has no child
                if not ptr.right.left and not ptr.right.right:
                    ptr.right = None
                    return
                # If ptr.right has 1 child
                elif (not ptr.right.left and ptr.right.right) or (ptr.right.left and not ptr.right.right):
                    ptr.right = ptr.right.left or ptr.right.right
                    return
            
            if key < ptr.key:
                ptr = ptr.left
            elif key > ptr.key:
                ptr = ptr.right

        # If key is found
        if ptr:
            successor_parent = ptr
            successor = ptr.right

            # Until successor is found
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Key value replaced with successor value
            ptr.key = successor.key
            ptr.val = successor.val

            # Removing successor
            if successor_parent == ptr:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right

    def getHash(self, key):
        hashValue = key % 10000
        return hashValue       


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



"""
Runtime: 164 ms, faster than 10.70% of Python3 online submissions for Design HashMap.
Memory Usage: 23.29 MB, less than 15.00% of Python3 online submissions for Design HashMap.
"""
# True HashSet using LinkedList
# TC: O(1), SC: O(n)
class ListNode:
    def __init__(self, key, val = None, nxt = None):
        self.key = key
        self.val = val
        self.nxt = nxt

    def __str__(self):
        return f"{self.key}, {self.val}, {self.nxt}"


class MyHashMap:
    def __init__(self):
        self.hashMap = [ListNode(None) for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        index = self.getHash(key)
        head = self.hashMap[index]

        if not head.nxt:
            head.nxt = ListNode(key, value)
        else:
            ptr = head
            while ptr.nxt and ptr.nxt.key <= key:
                ptr = ptr.nxt
            
            if ptr.key == key:
                ptr.val = value
            else:
                ptr.nxt = ListNode(key, value, ptr.nxt)

        print(head)

    def get(self, key: int) -> int:
        index = self.getHash(key)
        head = self.hashMap[index]

        ptr = head
        while ptr:
            if ptr.key == key:
                return ptr.val
            ptr = ptr.nxt

        return -1

    def remove(self, key: int) -> None:
        index = self.getHash(key)
        head = self.hashMap[index]

        ptr = head
        while ptr.nxt and ptr.nxt.key != key:
            ptr = ptr.nxt

        if ptr.nxt:
            ptr.nxt = ptr.nxt.nxt

    def getHash(self, key):
        hashValue = key % 10000
        return hashValue       


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)