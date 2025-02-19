"""
Accepted
1415 [Medium]
Runtime: 62 ms, faster than 20.79% of Python3 online submissions for The k-th Lexicographical String of All Happy Strings of Length n.
Memory Usage: 22.29 MB, less than 17.07% of Python3 online submissions for The k-th Lexicographical String of All Happy Strings of Length n.
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def backtrack(string, lis):
            if len(string) == n:
                res.append(string)
                return

            for char in lis:
                string += char
                if char == 'a':
                    backtrack(string, ['b', 'c'])
                elif char == 'b':
                    backtrack(string, ['a', 'c'])
                else:
                    backtrack(string, ['a', 'b'])
                string = string[:-1]

        backtrack("", ['a', 'b', 'c'])
        return res[k - 1] if k - 1 < len(res) else ""