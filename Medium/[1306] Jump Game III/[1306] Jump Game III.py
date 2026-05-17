"""
Accepted
1306 [Medium]
Runtime: 11 ms, faster than 65.93% of Python3 online submissions for Jump Game III.
Memory Usage: 26.37 MB, less than 80.96% of Python3 online submissions for Jump Game III.
"""
# Breadth First Search Solution
# TC: O(n), SC: O(n)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set()
        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True

            if i in visited:
                continue
            visited.add(i)

            if 0 <= i - arr[i]:
                queue.append(i - arr[i])
            if i + arr[i] < len(arr):
                queue.append(i + arr[i])
                
        return False



"""
Runtime: 11 ms, faster than 65.93% of Python3 online submissions for Jump Game III.
Memory Usage: 41.23 MB, less than 6.15% of Python3 online submissions for Jump Game III.
"""
# Depth First Search
# TC: O(n), SC: O(n)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        def dfs(i):
            if arr[i] == 0:
                return True

            visited.add(i)

            backward, forward = i - arr[i], i + arr[i]
            if 0 <= backward and backward not in visited and dfs(backward):
                return True
            if forward < len(arr) and forward not in visited and dfs(forward):
                return True

            return False

        return dfs(start)