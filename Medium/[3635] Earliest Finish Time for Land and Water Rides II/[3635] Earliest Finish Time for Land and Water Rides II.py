"""
Accepted
3635 [Medium]
Runtime: 131 ms, faster than 40.00% of Python3 online submissions for Earliest Finish Time for Land and Water Rides II.
Memory Usage: 34.82 MB, less than 50.91% of Python3 online submissions for Earliest Finish Time for Land and Water Rides II.
"""
# Greedy SOlution
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