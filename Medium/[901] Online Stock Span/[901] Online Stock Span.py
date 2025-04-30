"""
Accepted
901 [Medium]
Runtime: 40 ms, faster than 96.80% of Python online submissions for Online Stock Span.
Memory Usage: 22.25 MB, less than 86.07% of Python online submissions for Online Stock Span.
"""
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)



"""
Runtime: 8113 ms, faster than 5.02% of Python online submissions for Online Stock Span.
Memory Usage: 22.12 MB, less than 14.97% of Python online submissions for Online Stock Span.
"""
class StockSpanner:

    def __init__(self):
        self.monotonicStack = []

    def next(self, price: int) -> int:
        if self.monotonicStack:
            if self.monotonicStack[-1] > price:  
                self.monotonicStack.append(price)
            else:
                count = 1
                for i in self.monotonicStack[::-1]:
                    if i <= price:
                        count += 1
                    else:
                        break
                self.monotonicStack.append(price)
                return count
        else:
            self.monotonicStack.append(price)
        return 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)