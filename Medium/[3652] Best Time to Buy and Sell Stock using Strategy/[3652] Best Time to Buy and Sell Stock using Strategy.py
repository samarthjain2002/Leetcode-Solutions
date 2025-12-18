"""
Accepted
3652 [Medium]
Runtime: 287 ms, faster than 65.08% of Python3 online submissions for Best Time to Buy and Sell Stock using Strategy.
Memory Usage: 33.94 MB, less than 66.54% of Python3 online submissions for Best Time to Buy and Sell Stock using Strategy.
"""
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prefixSumsPrices = [prices[0]]
        for i in range(1, len(prices)):
            prefixSumsPrices.append(prefixSumsPrices[i - 1] + prices[i])

        prefixSumsStrategy = [strategy[0] * prices[0]]
        for i in range(1, len(prices)):
            prefixSumsStrategy.append(prefixSumsStrategy[i - 1] + (strategy[i] * prices[i]))

        totalSum = prefixSumsStrategy[-1]
        res = totalSum
        for i in range(len(prices) - k + 1):
            curSum = totalSum

            # Removing first k/2 elements
            if i == 0:
                curSum -= prefixSumsStrategy[i + k - 1]
            else:
                curSum -= prefixSumsStrategy[i + k - 1] - prefixSumsStrategy[i - 1]

            # Adding last k/2 elements
            curSum += prefixSumsPrices[i + k - 1] - prefixSumsPrices[i + (k // 2) - 1]

            res = max(res, curSum)
        return res