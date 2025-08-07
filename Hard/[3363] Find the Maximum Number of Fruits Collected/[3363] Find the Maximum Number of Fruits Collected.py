"""
Accepted
3363 [Hard]
Runtime: 3662 ms, faster than 5.26% of Python3 online submissions for Find the Maximum Number of Fruits Collected.
Memory Usage: 286.70 MB, less than 12.28% of Python3 online submissions for Find the Maximum Number of Fruits Collected.
"""
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)

        topleft = 0
        for i in range(N):
            topleft += fruits[i][i]

        def dfs(i, j, down):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i == N - 1 and j == N - 1:
                return 0
            if i == j or i > N - 1 or j > N - 1:
                return float("-inf")
            
            if down:
                op1 = dfs(i + 1, j - 1, True)
                op2 = dfs(i + 1, j, True)
                op3 = dfs(i + 1, j + 1, True)
            else:
                op1 = dfs(i - 1, j + 1, False)
                op2 = dfs(i, j + 1, False)
                op3 = dfs(i + 1, j + 1, False)

            cache[(i, j)] = fruits[i][j] + max(op1, op2, op3)
            return cache[(i, j)]
        

        cache = {}
        topright = dfs(0, N - 1, True)
        cache.clear()
        bottomleft = dfs(N - 1, 0, False)

        return topleft + topright + bottomleft