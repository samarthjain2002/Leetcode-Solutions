"""
Accepted
386 [Hard]
Runtime: 69 ms, faster than 81.34% of Python3 online submissions for Lexicographical Numbers.
Memory Usage: 25.06 MB, less than 9.09% of Python3 online submissions for Lexicographical Numbers.
"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(num):
            if num <= n:
                res.append(num)
                dfs(num * 10)
            else:
                return
            
            if num % 10 == 9:
                return
            else:
                dfs(num + 1)
        
        dfs(1)
        return res