"""
Accepted
2392 [Hard]
Runtime: 580 ms, faster than 67.94% of Python3 online submissions for Build a Matrix With Conditions.
Memory Usage: 25.18 MB, less than 95.42% of Python3 online submissions for Build a Matrix With Conditions.
"""
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Topological sort
        def find_order(pairs):
            graph = defaultdict(list)
            in_degree = defaultdict(int)
            nodes = set()

            for a,b in pairs:
                graph[a].append(b)
                in_degree[b] += 1
                nodes.add(a)
                nodes.add(b)

            zero_in_degree = deque([node for node in nodes if in_degree[node] == 0])
            order = []

            while zero_in_degree:
                node = zero_in_degree.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        zero_in_degree.append(neighbor)

            if len(order) == len(nodes):
                return order
            else:
                return []
    
        colConditions = find_order(colConditions)
        rowConditions = find_order(rowConditions)
        if not rowConditions or not colConditions:
            return []

        for i in range(1, k + 1):
            if i not in rowConditions:
                rowConditions.append(i)
            if i not in colConditions:
                colConditions.append(i)

        res = [[0] * k for _ in range(k)]
        for i, num in enumerate(rowConditions):
            res[i][colConditions.index(num)] = num
        return res