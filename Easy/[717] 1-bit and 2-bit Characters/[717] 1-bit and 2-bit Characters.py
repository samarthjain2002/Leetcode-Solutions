"""
Accepted
717 [Easy]
Runtime: 69 ms, faster than 25.93% of Python3 online submissions for 1-bit and 2-bit Characters.
Memory Usage: 17.80 MB, less than 67.66% of Python3 online submissions for 1-bit and 2-bit Characters.
"""
# TC: O(n), SC: O(1)
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        one_bit = False
        while i < len(bits):
            if bits[i] == 0:
                one_bit = True
                i += 1
            else:
                one_bit = False
                i += 2
        return one_bit