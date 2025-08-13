"""
Accepted
326 [Easy]
Runtime: 7 ms, faster than 73.20% of Python3 online submissions for Power of Three.
Memory Usage: 17.77 MB, less than 72.35% of Python3 online submissions for Power of Three.
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 3 == 0:
                n = n // 3
            else:
                return False
        return True



"""
Runtime: 16 ms, faster than 27.69% of Python3 online submissions for Power of Three.
Memory Usage: 17.99 MB, less than 25.52% of Python3 online submissions for Power of Three.
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0:
            return False

        cube = 1
        for _ in range(21):
            if cube == n:
                return True
            cube *= 3

        return False