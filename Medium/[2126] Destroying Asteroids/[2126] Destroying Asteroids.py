"""
Accepted
2126 [Medium]
Runtime: 804 ms, faster than 93.02% of Python3 online submissions for Destroying Asteroids.
Memory Usage: 31.22 MB, less than 37.38% of Python3 online submissions for Destroying Asteroids.
"""
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid <= mass:
                mass += asteroid
            else:
                return False
        return True