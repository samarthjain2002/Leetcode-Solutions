"""
Accepted
981 [Medium]
Runtime: 36 ms, faster than 99.33% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage:  74.67 MB, less than 14.91% of Python3 online submissions for Time Based Key-Value Store.
"""
class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
            
        sorted_list = self.dictionary[key]
        left, right = 0, len(sorted_list) - 1

        if sorted_list[right][0] <= timestamp:
            return sorted_list[right][1]
        if sorted_list[left][0] > timestamp:
            return ""

        while left != right - 1:
            mid = left + ((right - left) // 2)
            if sorted_list[mid][0] == timestamp:
                return sorted_list[mid][1]
            elif sorted_list[mid][0] < timestamp:
                left = mid
            else:
                right = mid
        return sorted_list[left][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)