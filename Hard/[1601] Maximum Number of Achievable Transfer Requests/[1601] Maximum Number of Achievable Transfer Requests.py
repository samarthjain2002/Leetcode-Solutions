"""
Accepted
1601 [Hard]
Runtime: 884 ms, faster than 40.37% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
Memory Usage: 17.91 MB, less than 100.00% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
"""
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0
        def backtrack(index, indegree, approved):
            nonlocal res

            if index == len(requests):
                for building in range(n):
                    if indegree[building] != 0:
                        return

                res = max(res, approved)
                return
            
            # Approve the request
            indegree[requests[index][0]] -= 1
            indegree[requests[index][1]] += 1
            backtrack(index + 1, indegree, approved + 1)

            # Backtrack the approval
            indegree[requests[index][0]] += 1
            indegree[requests[index][1]] -= 1
            backtrack(index + 1, indegree, approved)


        backtrack(0, defaultdict(int), 0)
        return res