"""
Accepted
787 [Medium]
Runtime: 117 ms, faster than 50.00% of Python3 online submissions for Cheapest Flights Within K Stops.
Memory Usage: 17.79 MB, less than 91.29% of Python3 online submissions for Cheapest Flights Within K Stops.
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Bellman-Ford algorithm
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tempPrices = prices.copy()
            for fro, to, cost in flights:
                if prices[fro] + cost < tempPrices[to]:
                    tempPrices[to] = prices[fro] + cost
            prices = tempPrices

        return  -1 if prices[dst] == float("inf") else prices[dst]