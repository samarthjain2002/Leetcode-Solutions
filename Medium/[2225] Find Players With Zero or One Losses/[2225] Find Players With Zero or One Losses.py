"""
Accepted
2225 [Medium]
Runtime: 1432 ms, faster than 80.74% of Python3 online submissions for Find Players With Zero or One Losses.
Memory Usage: 72.57 MB, less than 15.96% of Python3 online submissions for Find Players With Zero or One Losses.
"""
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        playerLosses = defaultdict(int)
        players = set()
        for winner, loser in matches:
            playerLosses[loser] += 1
            players.add(winner)
            players.add(loser)

        answer = [[], []]
        for player in players:
            if playerLosses[player] == 1:
                answer[1].append(player)
            elif playerLosses[player] == 0:
                answer[0].append(player)

        answer[0].sort()
        answer[1].sort()

        return answer