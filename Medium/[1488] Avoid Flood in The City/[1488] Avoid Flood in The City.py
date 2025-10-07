"""
Accepted
1488 [Medium]
Runtime: 387 ms, faster than 6.05% of Python3 online submissions for Avoid Flood in The City.
Memory Usage: 34.62 MB, less than 46.05% of Python3 online submissions for Avoid Flood in The City.
"""
# HashMap + Binary Search
# TC: O(nlog(n)), SC: O(n)
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)

        def find_earliest_day(latest_day):
            earliest_day = float("inf")
            low, high = 0, len(dry_days) - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                if dry_days[mid] >= latest_day:
                    earliest_day = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return earliest_day

        res = [-1] * N
        dry_days = []
        latest_rain_day = defaultdict(int)
        for i, lake_city in enumerate(rains):
            # Dry day
            if lake_city == 0:
                dry_days.append(i)
            # Rainy day
            else:
                # Has previously rained
                if lake_city in latest_rain_day:
                    # Latest day it had rained in this lake city
                    latest_day = latest_rain_day[lake_city]

                    # Earliest dry day after this latest day
                    earliest_day = find_earliest_day(latest_day)
                    # There are no available dry day after this lake is filled
                    if earliest_day >= len(dry_days):
                        return []

                    # Day chosen to dry this lake
                    day_to_dry = dry_days.pop(earliest_day)
                    res[day_to_dry] = lake_city
                
                # Keeping track of the latest day it rained in this lake_city
                latest_rain_day[lake_city] = i

        # Dry any lake (1 to inf) on the remaining dry days
        for day in dry_days:
            res[day] = 1
        
        return res