"""
Accepted
135 [Hard]
Runtime: 133 ms, faster than 22.85% of Python3 online submissions for Candy.
Memory Usage: 19.70 MB, less than 31.04% of Python3 online submissions for Candy.
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        if N == 1:
            return 1
        candies = [1] * N

        for i in range(1, N):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1
                
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)