"""
Accepted
394 [Medium]
Runtime: 34 ms, faster than 61.73% of Python3 online submissions for Decode String.
Memory Usage: 16.48 MB, less than 68.63% of Python3 online submissions for Decode String.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        stack = []
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        i = 0
        while i < N:
            if s[i] in digits:
                num = s[i]
                i += 1
                while s[i] != '[':
                    num += s[i]
                    i += 1
                stack.append(int(num))
                stack.append('[')
            elif s[i] == ']':
                temp = ""
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                num = stack.pop()
                stack.append(num * temp)
            else:
                stack.append(s[i])
            i += 1
            
        return "".join(stack)