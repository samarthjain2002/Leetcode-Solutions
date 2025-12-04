"""
Accepted
2211 [Medium]
Runtime: 115 ms, faster than 56.13% of Python3 online submissions for Count Collisions on a Road.
Memory Usage: 18.16 MB, less than 88.10% of Python3 online submissions for Count Collisions on a Road.
"""
# Simulation Solution
# TC: O(n), SC: O(1)
class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        right = 0
        stationary = False
        for car in directions:
            if car == 'R':
                right += 1
                stationary = False
            elif car == 'S':
                res += right
                right = 0
                stationary = True
            elif car == 'L':
                if right:
                    res += 2
                    right -= 1
                    res += right
                    right = 0
                    stationary = True
                elif stationary:
                    res += 1
        return res



"""
Runtime: 149 ms, faster than 44.24% of Python3 online submissions for Count Collisions on a Road.
Memory Usage: 19.79 MB, less than 5.95% of Python3 online submissions for Count Collisions on a Road.
"""
# Stack + Simulation Solution
# TC: O(n), SC: O(n)
class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        stack = [directions[0]]
        for car in directions[1 : ]:
            if car == 'L':
                if stack:
                    if stack[-1] == 'R':
                        stack.pop()
                        res += 2
                        stack.append('S')
                    elif stack[-1] == 'S':
                        res += 1
            else:
                stack.append(car)

        stationary = False
        for car in stack[ : : -1]:
            if car == 'S':
                stationary = True
            if car == 'R' and stationary:
                res += 1
        return res