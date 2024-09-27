"""
Accepted
729 [Medium]
Runtime: 173 ms, faster than 73.27% of Python3 online submissions for My Calendar I.
Memory Usage:  17.47 MB, less than 34.88% of Python3 online submissions for My Calendar I.
"""
class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        def binarySearch(start, end):
            low, high = 0, len(self.cal) - 1
            while low <= high:
                mid = (low + high) // 2
                if self.cal[mid][1] <= start:
                    low = mid + 1
                elif self.cal[mid][0] >= end:
                    high = mid - 1
                else:
                    return -1
            return low

        pos = binarySearch(start, end)
        if pos == -1:
            return False
        else:
            self.cal.insert(pos, [start, end])
            return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)