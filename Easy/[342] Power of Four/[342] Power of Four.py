"""
Accepted
342 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Power of Four.
Memory Usage: 17.82 MB, less than 38.66% of Python3 online submissions for Power of Four.
"""
import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n, 4) % 1 == 0



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Power of Four.
Memory Usage: 17.60 MB, less than 98.32% of Python3 online submissions for Power of Four.
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Power of Four.
Memory Usage: 17.95 MB, less than 18.40% of Python3 online submissions for Power of Four.
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False

        power = 1
        for i in range(16):
            if n == power:
                return True
            power *= 4
        return False