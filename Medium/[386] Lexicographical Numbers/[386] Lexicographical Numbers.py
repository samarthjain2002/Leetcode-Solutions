"""
Accepted
386 [Medium]
Runtime: 156 ms, faster than 5.06% of Python3 online submissions for Lexicographical Numbers.
Memory Usage: 22.79 MB, less than 29.24% of Python3 online submissions for Lexicographical Numbers.
"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(string):
            if int(string) > n:
                return

            res.append(int(string))

            for dig in "0123456789":
                dfs(string + dig)

        for dig in "123456789":
            dfs(dig)
        return res