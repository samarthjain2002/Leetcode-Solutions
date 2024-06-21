"""
Accepted
1552 [Medium]
Runtime: 929 ms, faster than 42.53% of Python3 online submissions for Magnetic Force Between Two Balls.
Memory Usage:  30.25 MB, less than 47.32% of Python3 online submissions for Magnetic Force Between Two Balls.
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def canPlaceBalls(min_dist):
            count = 1
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        low, high = 1, position[-1] - position[0]
        while low <= high:
            mid = (low + high) // 2
            if canPlaceBalls(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high