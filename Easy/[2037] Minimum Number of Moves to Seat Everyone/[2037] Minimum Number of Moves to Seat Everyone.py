"""
Accepted
2037 [Easy]
Runtime: 64 ms, faster than 27.12% of Python3 online submissions for Minimum Number of Moves to Seat Everyone.
Memory Usage: 16.44 MB, less than 82.54% of Python3 online submissions for Minimum Number of Moves to Seat Everyone.
"""
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        for i, seat in enumerate(seats):
            res += abs(seat - students[i])
        return res