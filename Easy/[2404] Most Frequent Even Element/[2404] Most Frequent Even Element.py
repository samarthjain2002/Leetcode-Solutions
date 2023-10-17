"""
Accepted
2404 [Easy]
Runtime: 249 ms, faster than 25.37% of Java online submissions for Most Frequent Even Element.
Memory Usage: 13.3 MB, less than 76.12% of Java online submissions for Most Frequent Even Element.
"""
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]%2 != 0:
                del nums[i]

        if len(nums) == 0:
            return -1
                
        nums.sort()

        freq = nums[0]
        freq_count = 0
        cur = nums[0]
        count = 0

        for i in range(0,len(nums)):
            if nums[i] == cur:
                count += 1
            else:
                if count > freq_count:
                    freq = cur
                    freq_count = count
                cur = nums[i]
                count = 1
        if count > freq_count:
            freq = cur

        return freq