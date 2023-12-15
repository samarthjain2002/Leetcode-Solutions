"""
Accepted
1436 [Easy]
Runtime: 67 ms, faster than 25.21% of Python3 online submissions for Destination City.
Memory Usage: 16.34 MB, less than 45.28% of Python3 online submissions for Destination City.
"""
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityA = []
        for cities in paths:
                cityA.append(cities[0])

        for cities in paths:
            if cities[1] not in cityA:
                return cities[1]