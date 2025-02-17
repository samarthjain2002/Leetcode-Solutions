"""
Accepted
1079 [Medium]
Runtime: 79 ms, faster than 14.91% of Python3 online submissions for Letter Tile Possibilities.
Memory Usage:  26.93 MB, less than 12.87% of Python3 online submissions for Letter Tile Possibilities.
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def backtrack(string, lis):
            for i in range(len(lis)):
                string += lis[i]
                backtrack(string, lis[ : i] + lis[i + 1 : ])
                res.add(string)
                string = string[:-1]

        backtrack("", list(tiles))
        return len(res)