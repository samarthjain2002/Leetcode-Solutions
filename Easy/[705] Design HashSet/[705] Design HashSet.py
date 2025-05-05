"""
Accepted
705 [Easy]
Runtime: 75 ms, faster than 40.97% of Python3 online submissions for Design HashSet.
Memory Usage: 23.05 MB, less than 51.40% of Python3 online submissions for Design HashSet.
"""
# Binary Search Tree Approach
# TC: O(log(n)), SC: O(n)
class BSTNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class MyHashSet:
    def __init__(self):
        self.root = BSTNode(-1)

    def add(self, key: int) -> None:
        ptr = self.root
        while True:
            if key < ptr.val and ptr.left:
                ptr = ptr.left
            elif key > ptr.val and ptr.right:
                ptr = ptr.right
            elif key == ptr.val:
                return
            else:
                break

        if key < ptr.val:
            ptr.left = BSTNode(key)
        elif key > ptr.val:
            ptr.right = BSTNode(key)

    def remove(self, key: int) -> None:
        ptr = self.root
        while ptr and ptr.val != key:
            if ptr.left and ptr.left.val == key:
                # If ptr.left has no children
                if not ptr.left.left and not ptr.left.right:
                    ptr.left = None
                    return
                # If ptr.left has 1 child
                elif (not ptr.left.left and ptr.left.right) or (ptr.left.left and not ptr.left.right):
                    ptr.left = ptr.left.left or ptr.left.right
                    return
            elif ptr.right and ptr.right.val == key:
                # If ptr.right has no child
                if not ptr.right.left and not ptr.right.right:
                    ptr.right = None
                    return
                # If ptr.right has 1 child
                elif (not ptr.right.left and ptr.right.right) or (ptr.right.left and not ptr.right.right):
                    ptr.right = ptr.right.left or ptr.right.right
                    return
            
            if key < ptr.val:
                ptr = ptr.left
            elif key > ptr.val:
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
            ptr.val = successor.val

            # Removing successor
            if successor_parent == ptr:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right
        

    def contains(self, key: int) -> bool:
        ptr = self.root
        while ptr:
            if ptr.val == key:
                return True
            elif key < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



"""
Runtime: 83 ms, faster than 38.47% of Python3 online submissions for Design HashSet.
Memory Usage: 24.36 MB, less than 25.48% of Python3 online submissions for Design HashSet.
"""
# True HashSet using LinkedList
# TC: O(1), SC: O(n)
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class MyHashSet:
    def __init__(self):
        self.hashSet = [ListNode(None) for _ in range(10000)]        

    def add(self, key: int) -> None:
        hashValue = key % 10000
        self.head = self.hashSet[hashValue]
        
        if not self.head.next:
            self.head.next = ListNode(key)        
        else:
            ptr = self.head
            while ptr.next and ptr.next.val <= key:
                ptr = ptr.next
            
            if ptr.val != key:
                ptr.next = ListNode(key, ptr.next)

    def remove(self, key: int) -> None:
        hashValue = key % 10000
        self.head = self.hashSet[hashValue]

        ptr = self.head
        while ptr.next and ptr.next.val != key:
            ptr = ptr.next

        if ptr.next:
            ptr.next = ptr.next.next        

    def contains(self, key: int) -> bool:
        hashValue = key % 10000
        self.head = self.hashSet[hashValue]

        ptr = self.head
        while ptr:
            if ptr.val == key:
                return True
            ptr = ptr.next

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



"""
Runtime: 3101 ms, faster than 5.00% of Python3 online submissions for Design HashSet.
Memory Usage: 23.05 MB, less than 51.25% of Python3 online submissions for Design HashSet.
"""
# BruteForced using LinkedList
# TC: O(n), SC: O(n)
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class MyHashSet:
    def __init__(self):
        self.head = ListNode(None)        

    def add(self, key: int) -> None:
        if not self.head.next:
            self.head.next = ListNode(key)        
        else:
            ptr = self.head
            while ptr.next and ptr.next.val <= key:
                ptr = ptr.next
            
            if ptr.val != key:
                ptr.next = ListNode(key, ptr.next)

    def remove(self, key: int) -> None:
        ptr = self.head
        while ptr.next and ptr.next.val != key:
            ptr = ptr.next

        if ptr.next:
            ptr.next = ptr.next.next        

    def contains(self, key: int) -> bool:
        ptr = self.head
        while ptr:
            if ptr.val == key:
                return True
            ptr = ptr.next

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)