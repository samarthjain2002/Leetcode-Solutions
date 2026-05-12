"""
Accepted
1665 [Hard]
Runtime: 363 ms, faster than 19.80% of Python3 online submissions for Minimum Initial Energy to Finish Tasks.
Memory Usage: 55.54 MB, less than 60.40% of Python3 online submissions for Minimum Initial Energy to Finish Tasks.
"""
# Binary Search on Answer Solution
# TC: O(nlogn), SC: O(1)
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort based on maximum remaining energy
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)
        
        def is_possible(energy):
            for ac, mini in tasks:
                if energy < mini:
                    return False
                energy -= ac
            return True

        res = 0
        # Binary search on answer
        low, high = 1, sum(mini for ac, mini in tasks)
        while low <= high:
            mid = low + ((high - low) // 2)
            if is_possible(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res



"""
Runtime: 55 ms, faster than 53.47% of Python3 online submissions for Minimum Initial Energy to Finish Tasks.
Memory Usage: 55.46 MB, less than 94.06% of Python3 online submissions for Minimum Initial Energy to Finish Tasks.
"""
# Sorting Approach
# TC: O(nlogn), SC: O(1)
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort based on maximum remaining energy
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)
        
        res = 0
        cur = 0
        for ac, mini in tasks:
            if cur < mini:
                res += mini - cur
                cur += mini - cur
            cur -= ac
        return res