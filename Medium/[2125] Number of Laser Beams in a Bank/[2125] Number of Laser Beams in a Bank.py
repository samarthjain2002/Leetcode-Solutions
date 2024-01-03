"""
Accepted
2125 [Medium]
Runtime: 127 ms, faster than 38.78% of Python3 online submissions for Number of Laser Beams in a Bank.
Memory Usage: 19.60 MB, less than 6.86% of Python3 online submissions for Number of Laser Beams in a Bank.
"""
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        secDevs = []
        for rows in bank:
            count = rows.count('1')
            if count != 0:
                secDevs.append(count)

        res = 0
        for i in range(1,len(secDevs)):
            res += secDevs[i] * secDevs[i - 1]
            
        return res