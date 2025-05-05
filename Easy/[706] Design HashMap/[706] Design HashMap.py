"""
Accepted
706 [Easy]
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