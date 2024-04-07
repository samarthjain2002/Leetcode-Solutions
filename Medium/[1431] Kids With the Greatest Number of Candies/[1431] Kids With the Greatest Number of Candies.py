"""
Accepted
1431 [Easy]
Runtime: 38 ms, faster than 73.54% of Python3 online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 16.52 MB, less than 47.33% of Python3 online submissions for Kids With the Greatest Number of Candies.
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        N = len(candies)
        res = []
        for i in range(N):
            if candies[i] + extraCandies >= M:
                res.append(True)
            else:
                res.append(False)
            
        return res