"""
Accepted
3160 [Medium]
Runtime: 99 ms, faster than 21.78% of Python3 online submissions for Find the Number of Distinct Colors Among the Balls.
Memory Usage: 63.39 MB, less than 31.85% of Python3 online submissions for Find the Number of Distinct Colors Among the Balls.
"""
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorFreq = defaultdict(int)
        colorCount = 0
        ballColors = defaultdict(int)

        res = []
        for query in queries:
            prevColor = ballColors[query[0]]
            if colorFreq[prevColor] != 0:
                colorFreq[prevColor] -= 1
                if colorFreq[prevColor] == 0:
                    colorCount -= 1
            ballColors[query[0]] = query[1]
            colorFreq[query[1]] += 1
            if colorFreq[query[1]] == 1:
                colorCount += 1
            res.append(colorCount)
        
        return res