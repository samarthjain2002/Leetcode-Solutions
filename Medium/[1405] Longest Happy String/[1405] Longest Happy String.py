"""
Accepted
1405 [Medium]
Runtime: 28 ms, faster than 92.01% of Python3 online submissions for Longest Happy String.
Memory Usage: 16.57 MB, less than 68.60% of Python3 online submissions for Longest Happy String.
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count:
                heapq.heappush(maxHeap, (count, char))

        longestHappyString = ""
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(longestHappyString) >= 2 and longestHappyString[-1] == longestHappyString[-2] == char:
                if not maxHeap:
                    break

                count2, char2 = heapq.heappop(maxHeap)
                longestHappyString += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                longestHappyString += char
                count += 1
            
            if count:
                heapq.heappush(maxHeap, (count, char))
        return longestHappyString