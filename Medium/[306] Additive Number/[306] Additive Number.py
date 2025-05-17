"""
Accepted
306 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Additive Number.
Memory Usage: 17.58 MB, less than 98.62% of Python3 online submissions for Additive Number.
"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        def backtrack(index, num1 = None, num2 = None):
            if index == len(num):
                if num1 is not None and num2 is not None:
                    return True
                else:
                    return False

            if num1 is None:
                if num[index] == '0':
                    if backtrack(index + 1, 0):
                        return True
                    else:
                        return False

                for i in range(index, len(num) - 2):
                    if backtrack(i + 1, int(num[index : i + 1])):
                        return True
            elif num2 is None:
                if num[index] == '0':
                    if backtrack(index + 1, num1, 0):
                        return True
                    else:
                        return False

                for i in range(index, len(num) - 1):
                    if backtrack(i + 1, num1, int(num[index : i + 1])):
                        return True
            else:
                nxt = num1 + num2
                if index + len(str(nxt)) - 1 >= len(num) or num[index : index + len(str(nxt))] != str(nxt):
                    return False
                
                if backtrack(index + len(str(nxt)), num2, nxt):
                    return True


        if backtrack(0):
            return True
        return False