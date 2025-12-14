"""
Accepted
2147 [Hard]
Runtime: 167 ms, faster than 99.05% of Python3 online submissions for Number of Ways to Divide a Long Corridor.
Memory Usage: 26.38 MB, less than 78.81% of Python3 online submissions for Number of Ways to Divide a Long Corridor.
"""
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        seatCount = corridor.count('S')
        if not seatCount or seatCount % 2:
            return 0

        firstSeat, lastSeat = corridor.index('S'), len(corridor) - corridor[::-1].index('S') - 1
        corridor = corridor[firstSeat: lastSeat + 1]

        res = 1
        count = 0
        first = False
        second = False
        for item in corridor:
            if second:
                if item == 'S':
                    second = False
                    first = True
                    res = res * count
                    res = res % MOD
                else:
                    count += 1
            elif first:
                if item == 'S':
                    first = False
                    second = True
                    count = 1
            else:
                first = True
        return res