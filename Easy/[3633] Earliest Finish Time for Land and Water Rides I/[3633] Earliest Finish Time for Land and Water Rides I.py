"""
Accepted
3633 [Easy]
Runtime: 7 ms, faster than 88.95 of Python3 online submissions for Earliest Finish Time for Land and Water Rides I.
Memory Usage: 19.39 MB, less than 56.98% of Python3 online submissions for Earliest Finish Time for Land and Water Rides I.
"""
# Greedy Solution
# TC: O(n+m), SC: O(1)
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def solve(firstRideTimes, firstRideDurations, secondRideTimes, secondRideDurations):
            firstRide = float("inf")
            for i in range(len(firstRideTimes)):
                firstRide = min(firstRide, firstRideTimes[i] + firstRideDurations[i])

            secondRide = float("inf")
            for j in range(len(secondRideTimes)):
                secondRide = min(secondRide, max(firstRide, secondRideTimes[j]) + secondRideDurations[j])

            return secondRide

        res = min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration)
        )
        return res



"""
Runtime: 267 ms, faster than 19.77 of Python3 online submissions for Earliest Finish Time for Land and Water Rides I.
Memory Usage: 19.49 MB, less than 18.02% of Python3 online submissions for Earliest Finish Time for Land and Water Rides I.
"""
# Brute-Force Solution
# TC: O(n*m), SC: O(1)
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float("inf")
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                landRideFirst = landStartTime[i] + landDuration[i]
                waterRideLater = max(landRideFirst, waterStartTime[j]) + waterDuration[j]

                waterRideFirst = waterStartTime[j] + waterDuration[j]
                landRideLater = max(waterRideFirst, landStartTime[i]) + landDuration[i]

                res = min(res, waterRideLater, landRideLater)
        return res



"""
Runtime: 326 ms, faster than 5.23% of Python3 online submissions for Earliest Finish Time for Land and Water Rides I.
Memory Usage: 19.33 MB, less than 56.98% of Python3 online submissions for Earliest Finish Time for Land and Water Rides I.
"""
# Brute-Force Solution
# TC: O(n*m), SC: O(1)
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float("inf")
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                cur = landStartTime[i] + landDuration[i]
                cur = max(cur, waterStartTime[j])
                cur += waterDuration[j]
                res = min(res, cur)

        for i in range(len(waterStartTime)):
            for j in range(len(landStartTime)):
                cur = waterStartTime[i] + waterDuration[i]
                cur = max(cur, landStartTime[j])
                cur += landDuration[j]
                res = min(res, cur)
        
        return res