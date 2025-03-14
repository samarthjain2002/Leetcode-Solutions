"""
Accepted
1011 [Medium]
Runtime: 210 ms, faster than 32.01% of Python3 online submissions for Capacity To Ship Packages Within D Days.
Memory Usage: 22.26 MB, less than 19.38% of Python3 online submissions for Capacity To Ship Packages Within D Days.
"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = 0
        low, high = max(weights), sum(weights)
        while low <= high:
            mid = low + ((high - low) // 2)

            count = 0
            numOfDays = 1
            for weight in weights:
                if numOfDays > days:
                    break
                    
                if count + weight <= mid:
                    count += weight
                else:
                    count = weight
                    numOfDays += 1
                
            if numOfDays <= days:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res