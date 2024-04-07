"""
Accepted
678 [Medium]
Runtime: 39 ms, faster than 33.04% of Python3 online submissions for Valid Parenthesis String.
Memory Usage:  16.55 MB, less than 50.32% of Python3 online submissions for Valid Parenthesis String.
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == '*':
                stars.append(i)
            else:
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while stack and stars:
            if stack[-1] < stars[-1]:
                stack.pop()
                stars.pop()
            else:
                break
        
        if stack:
            return False
        else:
            return True