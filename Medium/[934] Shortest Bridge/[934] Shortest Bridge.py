"""
Accepted
934 [Medium]
Runtime: 155 ms, faster than 13.93% of Python3 online submissions for Shortest Bridge.
Memory Usage: 20.43 MB, less than 25.30% of Python3 online submissions for Shortest Bridge.
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = deque()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        hashSet = set()
        def dfs(i, j, flag):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 0:
                return True
            if i in [-1, len(grid)] or j in [-1, len(grid[0])] or (i, j) in visited:
                return False

            visited.add((i, j))
            if flag:
                grid[i][j] = 2

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if dfs(nr, nc, flag) and not flag and (i, j) not in hashSet:
                    queue.append((i, j, 0))
                    hashSet.add((i, j))

        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j, flag)
                    flag = True

        
        visited = set()
        while queue:
            i, j, moves = queue.popleft()
            if grid[i][j] == 2:
                return moves - 1

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, moves + 1))



"""
Runtime: 164 ms, faster than 13.14% of Python3 online submissions for Shortest Bridge.
Memory Usage: 22.69 MB, less than 5.86% of Python3 online submissions for Shortest Bridge.
"""
# Bi-directional BFS (BFS from both islands)
class Solution:
    def shortestBridge(self, grid):
        queue = deque()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        def dfs(i, j, islandID):
            if grid[i][j] == 0 or (i, j) in visited:
                return

            visited.add((i, j))
            grid[i][j] = islandID

            # Enque only the boundary land cells (beach)
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                    queue.append((i, j, 0, islandID))
                    break
            
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    dfs(nr, nc, islandID)


        # Mark islands
        islandID = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j, islandID)
                    islandID += 1


        # Bi-directional BFS (BFS from both islands)
        dist_to_this_cell = {}
        # Visited now has all the land cells
        while queue:
            i, j, distance, islandID = queue.popleft()

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                # Bridge is complete
                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and ((grid[nr][nc] == 1 and islandID == 2) or (grid[nr][nc] == 2 and islandID == 1))):
                    return distance + dist_to_this_cell[(nr, nc)]

                # Building bridges from both sides
                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and
                    (nr, nc) not in visited):
                    grid[nr][nc] = islandID
                    visited.add((nr, nc))
                    queue.append((nr, nc, distance + 1, islandID))
                    dist_to_this_cell[(nr, nc)] = distance + 1