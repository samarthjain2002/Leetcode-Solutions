"""
Accepted
714 [Medium]
Runtime: 219 ms, faster than 33.68% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
Memory Usage: 27.27 MB, less than 29.21% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
"""
"""
prices = [1,3,2,8], fee = 2

Day	    Not Holding (dp[i][0])      Holding (dp[i][1])
0	    0	                        -3
1	    0	                        -3
2	    0	                        -3
3	    5	                        -3
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][1] = -prices[0] - fee

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
            
        return dp[len(prices) - 1][0]



"""
Runtime: 775 ms, faster than 5.03% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
Memory Usage:  201.86 MB, less than 10.35% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dpCache = {}
        
        def rec(i, holding):
            if i == len(prices):
                return 0
            if (i, holding) in dpCache:
                return dpCache[(i, holding)]

            if holding:
                op = prices[i] + rec(i + 1, True)
                cooldown = rec(i + 1, holding)
            else:
                op = -prices[i] - fee + rec(i + 1, True)
                cooldown = rec(i + 1, holding)
            dpCache[(i, holding)] = max(op, cooldown)

            return dpCache[(i, holding)]

        return rec(0, False)