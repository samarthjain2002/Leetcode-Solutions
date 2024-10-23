"""
Accepted
2477 [Medium]
Runtime: 235 ms, faster than 96.85% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
Memory Usage: 80.89 MB, less than 26.97% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
"""
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adjacencyMap = defaultdict(list)
        for a, b in roads:
            adjacencyMap[a].append(b)
            adjacencyMap[b].append(a)

        visited = set()
        res = 0
        def dfs(city):
            nonlocal res
            visited.add(city)
            if len(adjacencyMap[city]) == 1 and city != 0:
                res += 1
                return 1

            representatives = 0
            for c in adjacencyMap[city]:
                if c not in visited:
                    representatives += dfs(c)
            if city != 0:
                res += math.ceil((representatives + 1) / seats)
            return 1 + representatives

        dfs(0)
        return res