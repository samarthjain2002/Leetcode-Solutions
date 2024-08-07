"""
Accepted
2045 [Medium]
Runtime: 1720 ms, faster than 91.39% of Python3 online submissions for Second Minimum Time to Reach Destination.
Memory Usage:  26.38 MB, less than 78.81% of Python3 online submissions for Second Minimum Time to Reach Destination.
"""
<<<<<<< HEAD
=======
from collections import defaultdict
>>>>>>> 6a5c5c47e7221147fc1533f267f86b8977923eef
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        q = deque([1])
        cur_time = 0
        res = -1
        visit_times = defaultdict(list)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n:
                    if res != -1:
                        return cur_time
                    res = cur_time
                for nei in adj[node]:
                    nei_times = visit_times[nei]
                    if len(nei_times) == 0 or (len(nei_times) == 1 and nei_times[0] != cur_time):
                        q.append(nei)
                        nei_times.append(cur_time)

            if (cur_time //change) % 2 == 1:
                cur_time += change - (cur_time % change)
            cur_time += time