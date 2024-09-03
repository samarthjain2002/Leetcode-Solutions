"""
Accepted
1894 [Medium]
Runtime: 581 ms, faster than 42.80% of Python3 online submissions for Find the Student that Will Replace the Chalk.
Memory Usage: 30.53 MB, less than 48.71% of Python3 online submissions for Find the Student that Will Replace the Chalk.
"""
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefixSum = sum(chalk)
        k = k % prefixSum
        for i, prob in enumerate(chalk):
            if prob > k:
                return i
            else:
                k -= prob