"""
Accepted
841 [Medium]
Runtime: 64 ms, faster than 64.09% of Python3 online submissions for Keys and Rooms.
Memory Usage: 17.16 MB, less than 13.60% of Python3 online submissions for Keys and Rooms.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        adjList = defaultdict(list)
        for i, room in enumerate(rooms):
            for r in room:
                adjList[i].append(r)

        def dfs(adjList, source, visited):
            visited.add(source)
            for room in adjList[source]:
                if room not in visited:
                    dfs(adjList, room, visited)

        dfs(adjList, 0, visited)
        
        if len(visited) == len(rooms):
            return True
        else:
            return False