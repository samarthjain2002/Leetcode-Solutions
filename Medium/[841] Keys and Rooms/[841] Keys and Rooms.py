"""
Accepted
841 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Keys and Rooms.
Memory Usage: 18.15 MB, less than 74.04% of Python3 online submissions for Keys and Rooms.
"""
# Recursive DFS approach
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            
            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == len(rooms)



"""
Accepted
841 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Keys and Rooms.
Memory Usage: 18.18 MB, less than 74.04% of Python3 online submissions for Keys and Rooms.
"""
# Iterative approach
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        keys_have = rooms[0]
        while keys_have:
            for i in range(len(keys_have)):
                key = keys_have.pop()
                if key not in visited:
                    visited.add(key)
                    for new_key in rooms[key]:
                        keys_have.append(new_key)
        
        return len(visited) == len(rooms)



"""
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