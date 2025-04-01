"""
Accepted
403 [Hard]
Runtime: 120 ms, faster than 41.43% of Python3 online submissions for Frog Jump.
Memory Usage: 26.77 MB, less than 30.19% of Python3 online submissions for Frog Jump.
"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        visited = set()
        def backtrack(index, k):
            if index == len(stones) - 1:
                return True

            if (index, k) in visited:
                return False

            visited.add((index, k))

            for i in range(index + 1, len(stones)):
                dist = stones[i] - stones[index]
                if dist > k + 1:
                    break
                
                if dist in [k - 1, k, k + 1] and backtrack(i, dist):
                    return True

            return False

        
        return backtrack(1, 1)