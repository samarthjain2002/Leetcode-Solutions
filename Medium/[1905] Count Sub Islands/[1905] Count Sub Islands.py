"""
Accepted
1905 [Medium]
Runtime: 811 ms, faster than 18.00% of Python3 online submissions for Count Sub Islands.
Memory Usage: 72.04 MB, less than 5.06% of Python3 online submissions for Count Sub Islands.
"""
# DFS Solution
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def dfs(r, c):
            if (r < 0 or r == len(grid2) or c < 0 or c == len(grid2[0]) or 
                (r, c) in visited or grid2[r][c] == 0):
                return True

            visited.add((r, c))

            is_sub_island = True
            if grid1[r][c] == 0:
                is_sub_island = False

            for dx, dy in directions:
                is_sub_island = dfs(r + dx, c + dy) and is_sub_island
            
            return is_sub_island

        res = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i, j) not in visited and dfs(i, j):
                    res += 1
        return res



"""
Runtime: 2012 ms, faster than 5.15% of Python3 online submissions for Count Sub Islands.
Memory Usage: 123.88 MB, less than 5.06% of Python3 online submissions for Count Sub Islands.
"""
# Union-Find Solution
class UnionFind:
    def __init__(self, m, n):
        self.parent = {(r, c): (r, c) for r in range(m) for c in range(n)}
        self.rank = {(r, c): 1 for r in range(m) for c in range(n)}

    def find(self, cell):
        if cell != self.parent[cell]:
            self.parent[cell] = self.find(self.parent[cell])
        return self.parent[cell]

    def union(self, cell1, cell2):
        root1, root2 = self.find(cell1), self.find(cell2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        uf = UnionFind(len(grid1), len(grid1[0]))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Step 1: Union all land cells in grid2
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < len(grid2) and 0 <= nc < len(grid2[0]) and 
                            grid2[nr][nc] == 1):
                            uf.union((r, c), (nr, nc))

        # Step 2: Find unique island roots in grid2
        island_roots = defaultdict(list)
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1:
                    root = uf.find((r, c))
                    island_roots[root].append((r, c))

        # Step 3: Validate sub-islands
        sub_island_count = 0
        for root, cells in island_roots.items():
            if all(grid1[r][c] == 1 for r, c in cells):
                sub_island_count += 1
        return sub_island_count
