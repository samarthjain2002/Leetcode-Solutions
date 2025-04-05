"""
Accepted
1863 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Sum of All Subset XOR Totals.
Memory Usage: 17.58 MB, less than 96.02% of Python3 online submissions for Sum of All Subset XOR Totals.
"""
# TC: O(n)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res | num

        return res * 2**(len(nums) - 1)



"""
Runtime: 11 ms, faster than 76.73% of Python3 online submissions for Sum of All Subset XOR Totals.
Memory Usage: 17.69 MB, less than 83.05% of Python3 online submissions for Sum of All Subset XOR Totals.
"""
# TC: O(2^n)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(index, total):
            if index == len(nums):
                return total

            return dfs(index + 1, total) + dfs(index + 1, total ^ nums[index])

        return dfs(0, 0)
    

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def dfs(index, xor):
            nonlocal res
            if index == len(nums):
                res += xor
                return

            dfs(index + 1, xor)
            xor = xor ^ nums[index]
            dfs(index + 1, xor)

        dfs(0, 0)
        return res


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def dfs(index, xor):
            nonlocal res
            if index == len(nums):
                return

            dfs(index + 1, xor)
            xor = xor ^ nums[index]
            # Add only once because we skip adding when skipping index
            res += xor
            dfs(index + 1, xor)

        dfs(0, 0)
        return res