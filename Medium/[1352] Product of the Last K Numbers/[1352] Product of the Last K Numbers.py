"""
Accepted
1352 [Medium]
Runtime: 36 ms, faster than 60.43% of Python3 online submissions for Product of the Last K Numbers.
Memory Usage: 31.90 MB, less than 23.14% of Python3 online submissions for Product of the Last K Numbers.
"""
class ProductOfNumbers:

    def __init__(self):
        self.streamPrefix = []
        self.zero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.zero = len(self.streamPrefix)
            self.streamPrefix.append(1)
        else:
            if self.streamPrefix:
                self.streamPrefix.append(self.streamPrefix[-1] * num)
            else:
                self.streamPrefix.append(num)

    def getProduct(self, k: int) -> int:
        if k == len(self.streamPrefix):
            if self.zero < 0:
                return self.streamPrefix[-1]
            else:
                return 0
        elif self.zero < len(self.streamPrefix) - k:
            return self.streamPrefix[-1] // self.streamPrefix[-k - 1]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)