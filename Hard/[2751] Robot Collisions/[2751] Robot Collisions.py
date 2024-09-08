"""
Accepted
2751 [Hard]
Runtime: 1035 ms, faster than 41.88% of Python3 online submissions for Robot Collisions.
Memory Usage: 42.08 MB, less than 61.57% of Python3 online submissions for Robot Collisions.
"""
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [[positions[i], i, healths[i], directions[i]] for i in range(len(positions))]
        robots.sort()
        stack = []
        for robot in robots:
            while stack and stack[-1][3] == 'R' and robot[3] == 'L':
                if stack[-1][2] == robot[2]:
                    stack.pop()
                    break
                elif stack[-1][2] < robot[2]:
                    stack.pop()
                    robot[2] -= 1
                else:
                    stack[-1][2] -= 1
                    break
            else:
                stack.append(robot)

        def custom_sort_condition(item):
            return item[1]
        stack.sort(key = custom_sort_condition)

        return [stack[i][2] for i in range(len(stack))]