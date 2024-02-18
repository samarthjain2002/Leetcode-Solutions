"""
Accepted
2402 [Hard]
Runtime: 2427 ms, faster than 8.47% of Python3 online submissions for Meeting Rooms III.
Memory Usage: 63.28 MB, less than 32.24% of Python3 online submissions for Meeting Rooms III.
"""
from sortedcontainers import SortedDict

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        roomsUsed = SortedDict()
        rooms = [0] * n

        def freeRoom(rooms, start):
            minimum = [0, float("inf")]
            for i in range(n):
                if rooms[i] == 0:
                    return i, False
                elif start >= rooms[i]:
                    return i, False
                if minimum[1] > rooms[i]:
                    minimum[0] = i
                    minimum[1] = rooms[i]
            return minimum[0], True

        for i in range(n):
            roomsUsed[i] = 0

        for start, end in meetings:
            room, delay = freeRoom(rooms, start)
            roomsUsed[room] += 1
            if delay:
                rooms[room] += end - start
            else:
                rooms[room] = end

        res = [0, -1]
        for key, val in roomsUsed.items():
            if res[1] < val:
                res[0] = key
                res[1] = val

        return res[0]