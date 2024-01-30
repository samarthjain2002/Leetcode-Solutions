"""
Accepted
1921 [Medium]
Runtime: 819 ms, faster than 7.75% of Python3 online submissions for Eliminate Maximum Number of Monsters.
Memory Usage: 37.40 MB, less than 6.20% of Python3 online submissions for Eliminate Maximum Number of Monsters.
"""
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        list1 = []
        for i in range(0,len(dist)):
            list1.append([dist[i],speed[i]])

        def custom_sort_condition(element):
            return math.ceil(element[0]/element[1])

        list1.sort(key = custom_sort_condition)

        min = 0
        dest = 0
        for i in range(0,len(list1)):
            if math.ceil(list1[i][0]/list1[i][1]) > min:
                dest += 1
                min += 1
            else:
                break

        return dest