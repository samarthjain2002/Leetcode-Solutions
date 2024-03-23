"""
Accepted
881 [Medium]
Runtime: 337 ms, faster than 94.59% of Python3 online submissions for Boats to Save People.
Memory Usage:  23.51 MB, less than 8.81% of Python3 online submissions for Boats to Save People.
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        res = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                res += 1
                left += 1
                right -= 1
            else:
                right -= 1
                res += 1

        return res