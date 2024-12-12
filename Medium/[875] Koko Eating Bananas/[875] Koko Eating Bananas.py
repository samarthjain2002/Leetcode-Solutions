"""
Accepted
875 [Medium]
Runtime: 159 ms, faster than 41.54% of Python3 online submissions for Koko Eating Bananas.
Memory Usage:  18.46 MB, less than 11.07% of Python3 online submissions for Koko Eating Bananas.
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(num, hours):
            for pile in piles:
                hours = hours - math.ceil(pile / num)
            if hours < 0:
                return False
            else:
                return True            


        def bin_search(left, right):
            if possible(left, h):
                return left

            while left != right - 1:
                mid = left + ((right - left) // 2)
                poss = possible(mid, h)
                if not poss:
                    left = mid
                else:
                    right = mid
            return right


        return bin_search(1, max(piles))
    



"""
Runtime: 160 ms, faster than 67.72% of Python3 online submissions for Koko Eating Bananas.
Memory Usage:  18.45 MB, less than 50.76% of Python3 online submissions for Koko Eating Bananas.
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        N = len(piles)
        low, high = 1, max(piles)
        res = 0
        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for i, pile in enumerate(piles):
                hours += math.ceil(pile / mid)
            if hours <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res