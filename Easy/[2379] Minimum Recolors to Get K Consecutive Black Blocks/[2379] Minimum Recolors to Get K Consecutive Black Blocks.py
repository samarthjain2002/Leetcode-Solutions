"""
Accepted
2379 [Easy]
Runtime: 1 ms, faster than 41.86% of Java online submissions for Minimum Recolors to Get K Consecutive Black Blocks.
Memory Usage: 17.97 MB, less than 20.43% of Java online submissions for Minimum Recolors to Get K Consecutive Black Blocks.
"""
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = count = blocks[ : k].count('W')
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                count -= 1
            if blocks[i] == 'W':
                count += 1
            res = min(res, count)
        return res