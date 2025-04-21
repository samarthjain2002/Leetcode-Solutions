"""
Accepted
2145 [Medium]
Runtime: 167 ms, faster than 19.19% of Python3 online submissions for Count the Hidden Sequences.
Memory Usage: 32.31 MB, less than 57.58% of Python3 online submissions for Count the Hidden Sequences.
"""
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        maximum = minimum = curSum = 0
        for i in range(len(differences)):
            curSum += differences[i]
            maximum = max(maximum, curSum)
            minimum = min(minimum, curSum)
            
        return max(0, (upper - lower) - (maximum - minimum) + 1)



"""
Runtime: 477 ms, faster than 5.05% of Python3 online submissions for Count the Hidden Sequences.
Memory Usage: 32.31 MB, less than 57.58% of Python3 online submissions for Count the Hidden Sequences.
"""
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        maximum = minimum = curSum = differences[0]
        for i in range(1, len(differences)):
            curSum += differences[i]
            maximum = max(maximum, curSum)
            minimum = min(minimum, curSum)
            
        res = 0
        for i in range(lower, upper + 1):
            if i + minimum >= lower and i + maximum <= upper:
                res += 1
        return res