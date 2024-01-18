"""
Accepted
1154 [Easy]
Runtime: 55 ms, faster than 93.71% of Python3 online submissions for Day of the Year.
Memory Usage:  17.30 MB, less than 34.76% of Python3 online submissions for Day of the Year.
"""
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, date = int(date[0 : 4]), int(date[5 : 7]), int(date[8 : 10])
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False

        if leap == False:
            daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            daysInMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        day = 0
        for i in range(month - 1):
            day += daysInMonths[i]

        return day + date