
"""
Accepted
752 [Medium]
Runtime: 427 ms, faster than 36.72% of Python3 online submissions for Open the Lock.
Memory Usage: 19.27 MB, less than 58.87% of Python3 online submissions for Open the Lock.
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        visited = set(["0000"])
        while queue:
            lock, moves = queue.popleft()
            if lock == target:
                return moves

            for i in range(4):
                for diff in (-1, 1):
                    new_digit = (int(lock[i]) + diff) % 10      # -1 % 10 = 9 (In python)
                    new_lock = lock[ : i] + str(new_digit) + lock[i + 1 : ]

                    if new_lock not in deadends and new_lock not in visited:
                        queue.append((new_lock, moves + 1))
                        visited.add(new_lock)
            
        return -1