"""
Accepted
150 [Medium]
Runtime: 4 ms, faster than 30.77% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage:  19.08 MB, less than 5.60% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op in "+-*/":
                op1 = stack.pop()
                op2 = stack.pop()
                
            if op == '+':
                stack.append(op1 + op2)
            elif op == '-':
                stack.append(op2 - op1)
            elif op == '*':
                stack.append(op1 * op2)
            elif op == '/':
                stack.append(int(op2 / op1))
            else:
                stack.append(int(op))
                
        return stack[-1]