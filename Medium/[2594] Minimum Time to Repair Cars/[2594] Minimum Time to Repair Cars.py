"""
Accepted
2594 [Medium]
Runtime: 1077 ms, faster than 28.76% of Python3 online submissions for Minimum Time to Repair Cars.
Memory Usage: 22.03 MB, less than 19.17% of Python3 online submissions for Minimum Time to Repair Cars.
"""
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        res = 0

        low, high = 1, ranks[0] * cars * cars
        while low <= high:
            mid = low + ((high - low) // 2)

            repaired = 0
            for rank in ranks:
                repaired += math.sqrt(mid // rank) // 1
            
            if repaired >= cars:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res