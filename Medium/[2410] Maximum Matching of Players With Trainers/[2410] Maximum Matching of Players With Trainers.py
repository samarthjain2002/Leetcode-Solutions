"""
Accepted
2410 [Medium]
Runtime: 602 ms, faster than 67.77% of Python3 online submissions for Maximum Matching of Players With Trainers.
Memory Usage: 32.30 MB, less than 74.64% of Python3 online submissions for Maximum Matching of Players With Trainers.
"""
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left = 0
        res = 0
        for i, right in enumerate(trainers):
            if left < len(players) and players[left] <= right:
                res += 1
                left += 1
        return res