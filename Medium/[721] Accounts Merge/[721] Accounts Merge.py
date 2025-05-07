"""
Accepted
721 [Medium]
Runtime: 19 ms, faster than 92.22% of Python3 online submissions for Accounts Merge.
Memory Usage: 20.83 MB, less than 71.17% of Python3 online submissions for Accounts Merge.
"""
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return self.parent[node]

    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return

        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.parent[par1] = par2
        else:
            self.parent[par2] = par1
            self.rank[par1] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        emailToAcc = defaultdict(int)
        for i, account in enumerate(accounts):
            for email in account[1 : ]:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i

        emailGroup = defaultdict(list)
        for email, accIndex in emailToAcc.items():
            leader = uf.find(accIndex)
            emailGroup[leader].append(email)

        res = []
        for leader, emails in emailGroup.items():
            res.append([accounts[leader][0]] + sorted(emails))
        return res