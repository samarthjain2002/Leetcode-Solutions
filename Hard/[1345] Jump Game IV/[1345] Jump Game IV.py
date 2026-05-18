"""
Accepted
1345 [Hard]
Runtime: 305 ms, faster than 6.33% of Python3 online submissions for Jump Game IV.
Memory Usage: 33.10 MB, less than 88.92% of Python3 online submissions for Jump Game IV.
"""
# Breadth First Search Solution
# TC: O(n), SC: O(n)
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        ind = defaultdict(list)
        for i, num in enumerate(arr):
            ind[num].append(i)

        queue = deque([0])
        visited = set()
        steps = 0
        while queue:
            for _ in range(len(queue)):
                pos = queue.popleft()
                visited.add(pos)

                if pos == len(arr) - 1:
                    return steps

                neighbors = ind[arr[pos]] + [pos - 1, pos + 1]
                for nei in neighbors:
                    if 0 <= nei < len(arr) and nei not in visited:
                        queue.append(nei)

                ind[arr[pos]].clear()
                
            steps += 1