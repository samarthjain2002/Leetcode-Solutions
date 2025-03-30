"""
Accepted
752 [Medium]
Runtime: 427 ms, faster than 36.72% of Python3 online submissions for Open the Lock.
Memory Usage: 19.27 MB, less than 58.87% of Python3 online submissions for Open the Lock.
"""
# BFS approach
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



# DFS approach - Wrong
"""
deadends =
["7163", "3077", "5710", "2236", "8197", "5060", "3806", "7078", "3768", "8564", "7856", "8966", "8212", "3594", "0615", "3086", "6816", "1155", "5015", "9888", "5193", "7319", "7148", "3120", "9552", "9328", "2675", "3555", "5315", "6683", "6105", "0328", "0893"]
target =
"1781"
Output
11
Expected
7
"""
# 0000 -> 1000 -> 1900 -> 1800 -> 1700 -> 1700 -> 1790 -> 1780 -> 1781 (Only deepseek [DeepThink (R1)] answered correctly)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        dp = {}

        def rec(lock):
            if lock == target:
                return 0
            elif lock in deadends:
                return float("inf")
            elif lock in dp:
                return dp[lock]

            dp[lock] = float("inf")
            for i in range(4):
                if lock[i] == '9':
                    dp[lock] = min(dp[lock], 1 + rec(lock[ : i] + '0' + lock[i + 1 : ]))
                else:
                    dp[lock] = min(
                        dp[lock], 1 + rec(lock[ : i] + str(int(lock[i]) + 1) + lock[i + 1 : ])
                    )

                if lock[i] == '0':
                    dp[lock] = min(dp[lock], 1 + rec(lock[ : i] + '9' + lock[i + 1 : ]))
                else:
                    dp[lock] = min(
                        dp[lock], 1 + rec(lock[ : i] + str(int(lock[i]) - 1) + lock[i + 1 : ])
                    )

            return dp[lock]

        res = rec("0000")
        return res if res < float("inf") else -1