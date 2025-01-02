class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges) + 1:
            return False
            
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while node != par[node]:
                node = par[node]
            return node

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return True

            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]

            return False

        for edge in edges:
            a, b = edge[0], edge[1]
            if union(a, b):
                return False
        return True