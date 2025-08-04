"""
Accepted
1185 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Day of the Week.
Memory Usage: 18.06 MB, less than 11.71% of Python3 online submissions for Day of the Week.
"""
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        monthDays = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

        daysPassedSince1971Jan01 = (year - 1971) * 365  # Not counting leap years

        # Leap years before this year
        for y in range(1971, year):
            if y % 4 == 0:
                if y % 400 == 0:
                    daysPassedSince1971Jan01 += 1
                elif y % 100 == 0:
                    pass
                else:
                    daysPassedSince1971Jan01 += 1
        
        # Adding monthDays before this month
        for m in range(1, month):
            daysPassedSince1971Jan01 += monthDays[m]

        # Adding a day if this is a leap year and after Feb 29
        daysPassedSince1971Jan01 += day
        if month > 2:
            if year % 4 == 0:
                if year % 400 == 0:
                    daysPassedSince1971Jan01 += 1
                elif year % 100 == 0:
                    pass
                else:
                    daysPassedSince1971Jan01 += 1

        # Matching the day of the week to the number of days passed
        match daysPassedSince1971Jan01 % 7:
            case 1:
                return "Friday"
            case 2:
                return "Saturday"
            case 3:
                return "Sunday"
            case 4:
                return "Monday"
            case 5:
                return "Tuesday"
            case 6:
                return "Wednesday"
            case 0:
                return "Thursday"