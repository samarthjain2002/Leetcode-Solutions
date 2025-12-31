"""
Accepted
1970 [Hard]
Runtime: 1959 ms, faster than 6.63% of Python3 online submissions for Last Day Where You Can Still Cross.
Memory Usage: 26.29 MB, less than 48.07% of Python3 online submissions for Last Day Where You Can Still Cross.
"""
# TC: O(nlog(n)), SC: O(n)
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def check(i):
            water = set(tuple(cell) for cell in cells[ : i + 1])
            queue = deque()
            visited = set()
            for c in range(col):
                if (1, c + 1) not in water:
                    queue.append((1, c + 1))

            while queue:
                r, c = queue.popleft()
                if r == row:
                    return True

                if (r, c) in visited:
                    continue
                visited.add((r, c))

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 < nr <= row and 0 < nc <= col and (nr, nc) not in water:
                        queue.append((nr, nc))

            return False

        
        low, high = 0, len(cells) - 1
        res = 0
        while low <= high:
            mid = low + ((high - low) // 2)
            if check(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res + 1