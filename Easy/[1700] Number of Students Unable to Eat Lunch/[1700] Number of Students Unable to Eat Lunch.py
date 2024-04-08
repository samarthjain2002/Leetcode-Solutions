"""
Accepted
1700 [Easy]
Runtime: 35 ms, faster than 84.79% of Python3 online submissions for Number of Students Unable to Eat Lunch.
Memory Usage: 16.66 MB, less than 16.84% of Python3 online submissions for Number of Students Unable to Eat Lunch.
"""
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        N = len(students)
        ones = students.count(1)
        zeros = N - ones
        count = 0
        for sandwich in sandwiches:
            if sandwich == 0:
                if zeros == 0:
                    return N - count
                else:
                    count += 1
                    zeros -= 1
            else:
                if ones == 0:
                    return N - count
                else:
                    count += 1
                    ones -= 1
        return 0