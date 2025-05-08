"""
Accepted
310 [Medium]
Runtime: 58 ms, faster than 49.67% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 26.22 MB, less than 66.37% of Python3 online submissions for Minimum Height Trees.
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjMap = defaultdict(list)
        for edge in edges:
            a, b = edge
            adjMap[a].append(b)
            adjMap[b].append(a)

        edge_cnt = {}
        leaves = deque()
        for src, neighbors in adjMap.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edge_cnt[src] = len(neighbors)

        while leaves:
            if n <= 2:
                return list(leaves)

            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adjMap[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)