"""
Accepted
71 [Medium]
Runtime: 3 ms, faster than 36.46% of Python3 online submissions for Simplify Path.
Memory Usage: 17.95 MB, less than 29.34% of Python3 online submissions for Simplify Path.
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        string = ""
        for i in range(1, len(path)):
            if path[i] == '/':
                if not string:
                    pass
                elif string and string == '.':
                    pass
                elif string and string == "..":
                    if stack:
                        stack.pop()
                    else:
                        pass
                elif string:
                    stack.append(string)
                string = ""
            else:
                string += path[i]
                
        if string:
            if string == '.':
                pass
            elif string == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(string)

        return '/' + "/".join(stack)