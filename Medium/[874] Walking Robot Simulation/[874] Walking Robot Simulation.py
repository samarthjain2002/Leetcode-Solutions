"""
Accepted
874 [Medium]
Runtime: 294 ms, faster than 34.64% of Python3 online submissions for Walking Robot Simulation.
Memory Usage: 23.34 MB, less than 45.08% of Python3 online submissions for Walking Robot Simulation.
"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = [0,0]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]    # N, E, S, W
        d = 0
        
        hashSet = set()
        for obstacle in obstacles:
            hashSet.add(tuple(obstacle))
        
        res = 0
        for command in commands:
            if command < 0:
                if command == -1:
                    d += 1
                else:
                    d -= 1
                d = d % 4
            else:
                for step in range(command):
                    newCell = (pos[0] + directions[d][0], pos[1] + directions[d][1])
                    if newCell in hashSet:
                        break
                    else:
                        pos[0] += directions[d][0]
                        pos[1] += directions[d][1]
                res = max(res, pos[0] ** 2 + pos[1] ** 2)
        return res