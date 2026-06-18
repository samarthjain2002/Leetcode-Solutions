"""
Accepted
1344 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Angle Between Hands of a Clock.
Memory Usage: 19.60 MB, less than 12.42% of Python3 online submissions for Angle Between Hands of a Clock.
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = 0 if hour == 12 else hour

        hour_degree = (360 * (hour / 12)) + (360 * (1 / 12) * (minutes / 60))
        minutes_degree = 360 * (minutes / 60)

        degree_between_hands = abs(hour_degree - minutes_degree)

        return min(degree_between_hands, 360 - degree_between_hands)