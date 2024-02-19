"""
Accepted
231 [Easy]
Runtime: 37 ms, faster than 55.59% of Python3 online submissions for Power of Two.
Memory Usage: 16.60 MB, less than 53.28% of Python3 online submissions for Power of Two.
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (2**30 % n) == 0
    


"""
Accepted
231 [Easy]
Runtime: 30 ms, faster than 90.28% of Python3 online submissions for Power of Two.
Memory Usage: 16.50 MB, less than 96.02% of Python3 online submissions for Power of Two.
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
    


"""
Accepted
231 [Easy]
Runtime: 27 ms, faster than 96.66% of Python3 online submissions for Power of Two.
Memory Usage: 16.53 MB, less than 74.80% of Python3 online submissions for Power of Two.
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0 and math.pow(2, int(math.log2(n))) == n:
            return True
        else:
            return False