"""
Accepted
1926 [Medium]
Runtime: 103 ms, faster than 33.37% of Python3 online submissions for Nearest Exit from Entrance in Maze.
Memory Usage: 19.98 MB, less than 23.86% of Python3 online submissions for Nearest Exit from Entrance in Maze.
"""
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        queue = deque([tuple(entrance)])
        visited = set()
        visited.add(tuple(entrance))

        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Check if inbound, not visited, and is an empty cell
                    if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and (nx, ny) not in visited and maze[nx][ny] == '.':
                        # If it's an exit
                        if nx in [0, len(maze) - 1] or ny in [0, len(maze[0]) - 1]:
                            return steps
                            
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        return -1