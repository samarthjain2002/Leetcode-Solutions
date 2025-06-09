"""
Accepted
386 [Medium]
Runtime: 12 ms, faster than 62.06% of Python3 online submissions for Lexicographical Numbers.
Memory Usage: 21.15 MB, less than 92.91% of Python3 online submissions for Lexicographical Numbers.
"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1
        while len(res) < n:
            res.append(curr)

            if curr * 10 <= n:
                curr = curr * 10
            else:
                while curr % 10 == 9 or curr == n:
                    curr = curr // 10
                curr += 1
                
        return res



"""
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