"""
Accepted
3147 [Medium]
Runtime: 1194 ms, faster than 34.38% of Python3 online submissions for Taking Maximum Energy From the Mystic Dungeon.
Memory Usage: 31.82 MB, less than 15.00% of Python3 online submissions for Taking Maximum Energy From the Mystic Dungeon.
"""
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in reversed(range(len(energy))):
            if i + k < len(energy):
                energy[i] += energy[i + k]
    
        res = float("-inf")
        for i in range(len(energy)):
            res = max(res, energy[i])
        return res