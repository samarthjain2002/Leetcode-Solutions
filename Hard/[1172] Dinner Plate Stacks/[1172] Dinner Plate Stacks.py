"""
Accepted
1172 [Hard]
Runtime: 800 ms, faster than 9.73% of Python3 online submissions for Dinner Plate Stacks.
Memory Usage: 122.63 MB, less than 7.08% of Python3 online submissions for Dinner Plate Stacks.
"""
from sortedcontainers import SortedSet

class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = defaultdict(list)
        self.not_full = SortedSet()
        self.not_empty = SortedSet()

    def push(self, val: int) -> None:
        if len(self.not_full) == 0:
            index = len(self.not_empty)
        else:
            index = self.not_full[0]

        self.stacks[index].append(val)
        self.not_empty.add(index)
        self.not_full.add(index)
        if len(self.stacks[index]) == self.capacity:
            self.not_full.remove(index)

    def pop(self) -> int:
        if len(self.not_empty) == 0:
            return -1
        else:
            index = self.not_empty[-1]

        val = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            self.not_empty.remove(index)
        self.not_full.add(index)
        
        return val

    def popAtStack(self, index: int) -> int:
        if len(self.stacks[index]) == 0:
            return -1
        else:
            val = self.stacks[index].pop()
            if len(self.stacks[index]) == 0:
                self.not_empty.remove(index)
            self.not_full.add(index)
            
            return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)