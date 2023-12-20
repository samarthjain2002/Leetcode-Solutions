"""
Accepted
2706 [Easy]
Runtime: 58 ms, faster than 88.58% of Python3 online submissions for Buy Two Chocolates.
Memory Usage: 17.24 MB, less than 23.41% of Python3 online submissions for Buy Two Chocolates.
"""
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if (prices[0] + prices[1]) > money:
            return money
        return money - (prices[0] + prices[1])