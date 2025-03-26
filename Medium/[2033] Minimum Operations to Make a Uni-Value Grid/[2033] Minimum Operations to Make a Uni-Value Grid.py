"""
Accepted
2033 [Medium]
Runtime: 284 ms, faster than 16.67% of Python3 online submissions for Minimum Operations to Make a Uni-Value Grid.
Memory Usage: 39.05 MB, less than 50.44% of Python3 online submissions for Minimum Operations to Make a Uni-Value Grid.
"""
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        totalSum = 0
        for row in grid:
            for ele in row:
                arr.append(ele)
                totalSum += ele
                if ele % x != grid[0][0] % x:
                    return -1
        arr.sort()
                    
        prefixSum = 0
        res = float("inf")
        for i, ele in enumerate(arr):
            cost_left = (ele * i) - prefixSum
            cost_right = (totalSum - ele - prefixSum) - (ele * (len(arr) - i - 1))
            operations = (cost_left + cost_right) // x
            res = min(res, operations)
            prefixSum += ele
        return res