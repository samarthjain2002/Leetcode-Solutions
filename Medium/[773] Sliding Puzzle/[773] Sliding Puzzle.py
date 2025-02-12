"""
Accepted
773 [Hard]
Runtime: 4 ms, faster than 83.27% of Python3 online submissions for Sliding Puzzle.
Memory Usage: 17.83 MB, less than 60.17% of Python3 online submissions for Sliding Puzzle.
"""
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adj = {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4],
            4: [1,3,5],
            5: [2,4],
        }
        b = "".join(str(ele) for row in board for ele in row)

        visited = set()
        queue = deque([(b.index('0'), b, 0)])
        while queue:
            index, b, moves = queue.popleft()

            if b == "123450":
                return moves

            b_arr = list(b)
            for i in adj[index]:
                new_b_arr = b_arr.copy()
                new_b_arr[index], new_b_arr[i] = new_b_arr[i], new_b_arr[index]
                new_b = "".join(new_b_arr)
                
                if new_b not in visited:
                    queue.append((i, new_b, moves + 1))
                    visited.add((new_b))

        return -1