"""
Accepted
826 [Medium]
Runtime: 295 ms, faster than 59.71% of Python3 online submissions for Most Profit Assigning Work.
Memory Usage: 18.74 MB, less than 100.00% of Python3 online submissions for Most Profit Assigning Work.
"""
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        N = len(profit)
        M = len(worker)
        def custom_sort_condition(index):
            return profit[index]
        
        indices = list(range(N))
        indices.sort(key = custom_sort_condition)

        difficulty = [difficulty[i] for i in indices]
        profit = [profit[i] for i in indices]
        worker.sort()

        left, right = N - 1, M - 1
        res = 0
        while right >= 0 and left >= 0:
            if difficulty[left] <= worker[right]:
                res += profit[left]
                right -= 1
            else:
                left -= 1
        return res