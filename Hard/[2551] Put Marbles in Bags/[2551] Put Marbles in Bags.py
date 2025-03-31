"""
Accepted
2551 [Hard]
Runtime: 119 ms, faster than 95.04% of Python3 online submissions for Put Marbles in Bags.
Memory Usage: 30.26 MB, less than 62.81% of Python3 online submissions for Put Marbles in Bags.
"""
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        splits = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        splits.sort()

        max_score = weights[0] + weights[-1] + sum(splits[-(k - 1) : ])
        min_score = weights[0] + weights[-1] + sum(splits[ : k - 1])

        return max_score - min_score