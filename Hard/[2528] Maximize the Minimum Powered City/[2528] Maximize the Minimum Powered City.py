"""
Accepted
2528 [Hard]
Runtime: 1075 ms, faster than 90.72% of Python3 online submissions for Maximize the Minimum Powered City.
Memory Usage: 35.33 MB, less than 27.84% of Python3 online submissions for Maximize the Minimum Powered City.
"""
# PrefixSum + Difference Array + Binary Search on Answer + Greedy Solution
# TC: O(nlog(k)), SC: O(n)
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        prefixSums = [stations[0]]
        for i in range(1, len(stations)):
            prefixSums.append(prefixSums[i - 1] + stations[i])

        powerStations = [0] * len(stations)
        for i in range(len(stations)):
            powerStations[i] = prefixSums[min(len(stations) - 1, i + r)]
            if i - r - 1 >= 0:
                powerStations[i] -= prefixSums[max(0, i - r - 1)]

        def canAdd(mid, k):
            diff_arr = [0] * len(stations)
            cur = 0
            for i, power in enumerate(powerStations):
                cur += diff_arr[i]
                total = power + cur

                if total < mid:
                    need = mid - total
                    if need > k:
                        return False

                    k -= need
                    cur += need

                    diff_arr[i] += need
                    if i + (2 * r) + 1 < len(diff_arr):
                        diff_arr[i + (2 * r) + 1] -= need

            return True

        low, high = min(powerStations), max(powerStations) + k
        res = low
        while low <= high:
            mid = low + ((high - low) // 2)

            if canAdd(mid, k):
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res