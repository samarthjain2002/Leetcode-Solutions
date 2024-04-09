"""
Accepted
2073 [Easy]
Runtime: 32 ms, faster than 96.94% of Python3 online submissions for Time Needed to Buy Tickets.
Memory Usage: 16.53 MB, less than 51.83% of Python3 online submissions for Time Needed to Buy Tickets.
"""
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = tickets[k]
        N = len(tickets)
        for i in range(k):      #People standing infront of the person
            if tickets[i] <= tickets[k]:
                res += tickets[i]
            else:
                res += tickets[k]

        for i in range(k + 1, N):   #People standing behind the person
            if tickets[i] < tickets[k]:
                res += tickets[i]
            else:
                res += tickets[k] - 1

        return res