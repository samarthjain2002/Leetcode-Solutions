"""
Accepted
735 [Medium]
Runtime: 83 ms, faster than 52.22% of Python3 online submissions for Asteroid Collision.
Memory Usage: 18.00 MB, less than 11.08% of Python3 online submissions for Asteroid Collision.
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i, asteroid in enumerate(asteroids):
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                else:
                    break
            else:
                stack.append(asteroid)
        return stack