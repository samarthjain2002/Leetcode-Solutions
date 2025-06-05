"""
Accepted
1052 [Medium]
Runtime: 221 ms, faster than 36.28% of Python3 online submissions for Grumpy Bookstore Owner.
Memory Usage: 18.89 MB, less than 64.93% of Python3 online submissions for Grumpy Bookstore Owner.
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(grumpy)
        left = 0
        window, maxWindow = 0, 0
        satisfied = 0
        for right in range(N):
            if grumpy[right]:
                window += customers[right]
            else:
                satisfied += customers[right]

            if right - left > minutes - 1:
                if grumpy[left]:
                    window -= customers[left]
                left += 1
            maxWindow = max(maxWindow, window)

        return satisfied + maxWindow