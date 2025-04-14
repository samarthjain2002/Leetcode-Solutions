"""
Accepted
1041 [Medium]
Runtime: 377 ms, faster than 95.99% of Python3 online submissions for Robot Bounded In Circle.
Memory Usage: 17.72 MB, less than 65.08% of Python3 online submissions for Robot Bounded In Circle.
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = {d: False for d in "NEWS"}
        direction['N'] = True

        left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

        pos = [0, 0]
        for i in instructions:
            if i == 'G':
                if direction['N']:
                    pos[1] += 1
                elif direction['E']:
                    pos[0] += 1
                elif direction['W']:
                    pos[0] -= 1
                else:
                    pos[1] -= 1
            elif i == 'L':
                for i in "NEWS":
                    if direction[i]:
                        d = i
                direction[d] = False
                direction[left[d]] = True
            else:
                for i in "NEWS":
                    if direction[i]:
                        d = i
                direction[d] = False
                direction[right[d]] = True
                
        return pos == [0, 0] or pos != [0, 0] and not direction['N']