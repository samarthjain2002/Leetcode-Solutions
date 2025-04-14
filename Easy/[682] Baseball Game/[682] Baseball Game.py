"""
Accepted
682 [Easy]
Runtime: 377 ms, faster than 95.99% of Python3 online submissions for Baseball Game.
Memory Usage: 17.94 MB, less than 62.01% of Python3 online submissions for Baseball Game.
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)