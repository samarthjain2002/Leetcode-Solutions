"""
Accepted
2561 [Hard]
Runtime: 187 ms, faster than 9.92% of Python3 online submissions for Rearranging Fruits.
Memory Usage: 55.90 MB, less than 6.61% of Python3 online submissions for Rearranging Fruits.
"""
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        basket1Freq, basket2Freq = defaultdict(int), defaultdict(int)
        fruits = defaultdict(int)
        for i in range(len(basket1)):
            basket1Freq[basket1[i]] += 1
            basket2Freq[basket2[i]] += 1
            fruits[basket1[i]] += 1
            fruits[basket2[i]] += 1

        for fruit, count in fruits.items():
            if count % 2:
                return -1

        basket1.sort()
        basket2.sort()

        lowestCost = min(min(basket1), min(basket2))

        extra1, extra2 = [], []
        for key in fruits.keys():
            if basket1Freq[key] > basket2Freq[key]:
                extra1.extend([key] * (basket1Freq[key] - (fruits[key] // 2)))
            elif basket2Freq[key] > basket1Freq[key]:
                extra2.extend([key] * (basket2Freq[key] - (fruits[key] // 2)))

        extra1.sort()
        extra2.sort(reverse=True)
        
        res = 0
        for x, y in zip(extra1, extra2):
            res += min(lowestCost * 2, min(x, y))
        return res