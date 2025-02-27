"""
Accepted
781 [Medium]
Runtime: 38 ms, faster than 90.40% of Python3 online submissions for Rabbits in Forest.
Memory Usage: 16.54 MB, less than 96.56% of Python3 online submissions for Rabbits in Forest.
"""
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = defaultdict(int)
        for answer in answers:
            rabbits[answer] += 1
            
        res = 0
        for key, val in rabbits.items():
            while val > 0:
                res += key + 1
                val -= key + 1
        return res