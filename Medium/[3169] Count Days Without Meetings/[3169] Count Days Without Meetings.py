"""
Accepted
3169 [Medium]
Runtime: 192 ms, faster than 43.32% of Python3 online submissions for Count Days Without Meetings.
Memory Usage: 52.96 MB, less than 30.73% of Python3 online submissions for Count Days Without Meetings.
"""
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        day = 1
        res = 0
        for meeting in meetings:
            if day < meeting[0]:
                res += meeting[0] - day
            day = max(day, meeting[1] + 1)
        return res + days - day + 1 if days >= day else res