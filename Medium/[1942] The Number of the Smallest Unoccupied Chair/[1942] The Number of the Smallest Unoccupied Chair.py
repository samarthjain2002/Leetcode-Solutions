"""
Accepted
1942 [Medium]
Runtime: 3629 ms, faster than 9.91% of Python3 online submissions for The Number of the Smallest Unoccupied Chair.
Memory Usage: 22.84 MB, less than 60.06% of Python3 online submissions for The Number of the Smallest Unoccupied Chair.
"""
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for i, (arr, leav) in enumerate(times):
            events.append([arr, i, "Arrive"])
            events.append([leav, i, "Leaving"])

        events.sort(key = lambda x:(x[0], x[2] == "Arrive"))

        chairs = [False] * len(times)
        chairToFriend = [-1] * len(times)

        for time, friend, event in events:
            if event == "Leaving":
                chairs[chairToFriend[friend]] = False
            else:
                for i, chair in enumerate(chairs):
                    if not chair:
                        chairs[i] = True
                        chairToFriend[friend] = i
                        if friend == targetFriend:
                            return i
                        break