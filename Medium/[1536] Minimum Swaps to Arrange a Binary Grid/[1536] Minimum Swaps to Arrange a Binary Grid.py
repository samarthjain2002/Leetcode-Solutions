"""
Accepted
1536 [Medium]
Runtime: 11 ms, faster than 50.00% of Python3 online submissions for Minimum Swaps to Arrange a Binary Grid.
Memory Usage: 20.71 MB, less than 87.88% of Python3 online submissions for Minimum Swaps to Arrange a Binary Grid.
"""
# Greedy + Simulation Solution
# TC: O(n^2), SC: O(n)
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)

        zs = []
        for row in range(N):
            count = 0
            for col in reversed(range(N)):
                if grid[row][col] == 1:
                    zs.append(count)
                    break
                else:
                    count += 1
            else:
                zs.append(count)
        
        req = N - 1
        res = 0
        for i in range(N):
            for j in range(i, N):
                if zs[j] >= req:
                    res += j - i
                    zs.insert(i, zs.pop(j))
                    req -= 1
                    break
            else:
                return -1
        return res