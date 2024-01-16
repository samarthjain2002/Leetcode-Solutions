"""
Accepted
380 [Medium]
Runtime: 474 ms, faster than 30.81% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage:  64.68 MB, less than 19.71% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
class RandomizedSet:

    def __init__(self):
        self.randomSet = set()        

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        self.randomSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False
        self.randomSet.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.randomSet))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()