"""
Accepted
895 [Hard]
Runtime: 77 ms, faster than 65.97% of Python3 online submissions for Maximum Frequency Stack.
Memory Usage: 26.54 MB, less than 37.86% of Python3 online submissions for Maximum Frequency Stack.
"""
class FreqStack:
    def __init__(self):
        self.groups = defaultdict(list)
        self.freq = defaultdict(int)
        self.maximum = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.maximum = max(self.maximum, self.freq[val])
        self.groups[self.freq[val]].append(val)

    def pop(self) -> int:
        res = self.groups[self.maximum].pop()
        self.freq[res] -= 1
        if len(self.groups[self.maximum]) == 0:
            self.maximum -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()