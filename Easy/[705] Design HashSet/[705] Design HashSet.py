"""
Accepted
705 [Easy]
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