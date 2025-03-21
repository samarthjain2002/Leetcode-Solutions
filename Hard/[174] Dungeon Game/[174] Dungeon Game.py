"""
Accepted
174 [Hard]
Runtime: 133 ms, faster than 22.85% of Python3 online submissions for Dungeon Game.
Memory Usage: 19.70 MB, less than 31.04% of Python3 online submissions for Dungeon Game.
"""
# Bottom-up Tabulation Dynamic Programming approach
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[float("inf")] * (len(dungeon[0]) + 1) for _ in range(len(dungeon) + 1)]
        # So that the last cell doesn't add infinity
        dp[len(dungeon)][len(dungeon[0]) - 1] = 0

        for i in reversed(range(len(dungeon))):
            for j in reversed(range(len(dungeon[0]))):
                if dungeon[i][j] < 0:
                    # Health required to face the demon in this cell
                    dp[i][j] = abs(dungeon[i][j])
                else:
                    # Health attained (in negative)
                    dp[i][j] = -1 * dungeon[i][j]
                # Health required to reach the princess from this cell
                dp[i][j] += min(dp[i + 1][j], dp[i][j + 1])

                # No initial health required from this cell
                if dp[i][j] < 0:
                    dp[i][j] = 0

        # Atleast +1 health at any moment
        return dp[0][0] + 1



# Top-down Memoization Dynamic Programming approach
# MLE
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        cache = {}

        def dfs(i, j, health, damage, minReq):
            if i == len(dungeon) or j == len(dungeon[0]):
                return float("inf")

            if (i, j, minReq) in cache:
                return cache[(i, j, minReq)]

            if dungeon[i][j] < 0:
                if health + dungeon[i][j] < 1:  # Need more health to survive
                    minReq += abs(health + dungeon[i][j]) + 1
                    health = 1  # Reset to minimum survival health
                else:
                    health += dungeon[i][j]  # Deduct health normally
            elif dungeon[i][j] > 0:
                health += dungeon[i][j] 

            if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                return minReq

            cache[(i, j, minReq)] = min(dfs(i, j + 1, health, damage, minReq), dfs(i + 1, j, health, damage, minReq))
            return cache[(i, j, minReq)]

        
        return dfs(0, 0, 1, 0, 1)