"""
Accepted
1823 [Medium]
Runtime: 132 ms, faster than 23.59% of Python3 online submissions for Find the Winner of the Circular Game.
Memory Usage: 16.49 MB, less than 84.30% of Python3 online submissions for Find the Winner of the Circular Game.
"""
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque([_ for _ in range(1, n + 1)])

        while len(queue) > 1:
            for i in range(k - 1):
                pop = queue.popleft()
                queue.append(pop)
            queue.popleft()
        
        return queue[0]