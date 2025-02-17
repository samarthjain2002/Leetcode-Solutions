"""
Accepted
1079 [Medium]
Runtime: 35 ms, faster than 64.77% of Python3 online submissions for Letter Tile Possibilities.
Memory Usage:  26.89 MB, less than 15.04% of Python3 online submissions for Letter Tile Possibilities.
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def backtrack(string, lis):
            for i in range(len(lis)):
                string += lis[i]
                if string not in res:
                    backtrack(string, lis[ : i] + lis[i + 1 : ])
                res.add(string)
                string = string[:-1]

        backtrack("", list(tiles))
        return len(res)