"""
Accepted
380 [Medium]
Runtime: 146 ms, faster than 44.50% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 58.01 MB, less than 20.16% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.array = []  

    def insert(self, val: int) -> bool:
        if val in self.dict.keys():
            return False

        self.dict[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict.keys():
            return False

        index = self.dict[val]
        # Change the index of last element in array
        self.dict[self.array[-1]] = index
        # Switch the val to be removed with last element
        self.array[index] = self.array[-1]
        self.array.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        index = random.randrange(len(self.array))
        return self.array[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()