"""
Accepted
2349 [Easy]
Runtime: 683 ms, faster than 15.69% of Python3 online submissions for Design a Number Container System.
Memory Usage: 151.65 MB, less than 18.14% of Python3 online submissions for Design a Number Container System.
"""
from sortedcontainers import SortedSet
from collections import defaultdict

class NumberContainers:
    def __init__(self):
        self.indexToNumber = defaultdict(int)
        self.numberToIndices = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if self.indexToNumber[index] != 0:
            prevNumber = self.indexToNumber[index]
            self.numberToIndices[prevNumber].remove(index)
            if not self.numberToIndices[prevNumber]:
                del self.numberToIndices[prevNumber]

        self.indexToNumber[index] = number
        self.numberToIndices[number].add(index)

    def find(self, number: int) -> int:
        if number in self.numberToIndices:
            return self.numberToIndices[number][0]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)