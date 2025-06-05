"""
Accepted
1061 [Medium]
Runtime: 3 ms, faster than 94.40% of Python3 online submissions for Lexicographically Smallest Equivalent String.
Memory Usage: 17.88 MB, less than 63.50% of Python3 online submissions for Lexicographically Smallest Equivalent String.
"""
class UnionFind:
    def __init__(self):
        self.par = {chr(asc): chr(asc) for asc in range(97, 97 + 26)}
        self.rank = {chr(asc): 1 for asc in range(97, 97 + 26)}
        self.lex_small = {chr(asc): chr(asc) for asc in range(97, 97 + 26)}

    def find(self, node):
        while self.par[node] != node:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return self.par[node]

    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)

        if par1 == par2:
            return 

        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            if self.lex_small[par2] < self.lex_small[par1]:
                self.lex_small[par1] = self.lex_small[par2]
        elif self.rank[par1] < self.rank[par2]:
            self.par[par1] = par2
            if self.lex_small[par2] > self.lex_small[par1]:
                self.lex_small[par2] = self.lex_small[par1]
        else:
            self.par[par2] = par1
            if self.lex_small[par2] < self.lex_small[par1]:
                self.lex_small[par1] = self.lex_small[par2]
            self.rank[par1] += 1


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()

        for i in range(len(s1)):
            uf.union(s1[i], s2[i])

        res = ""
        for char in baseStr:
            par = uf.find(char)
            res += uf.lex_small[par]
        return res