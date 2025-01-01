"""
Accepted
684 [Medium]
Runtime: 6 ms, faster than 33.26% of Python3 online submissions for Redundant Connection.
Memory Usage: 18.46 MB, less than 8.58% of Python3 online submissions for Redundant Connection.
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Because in a DAG, n == len(edges) - 1
        n = len(edges)      # This graph contains one extra edge

        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node):
            while par[node] != node:
                node = par[node]
            return node

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # If both n1 and n2 have same root ancestor/parent, adding the edge makes a cycle
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]

            return True
        
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            if not union(n1, n2):
                return edge