"""
Accepted
2134 [Medium]
Runtime: 726 ms, faster than 50.00% of Python3 online submissions for Minimum Swaps to Group All 1's Together II.
Memory Usage: 20.80 MB, less than 29.05% of Python3 online submissions for Minimum Swaps to Group All 1's Together II.
"""
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        numOnes = sum(nums)  # Count the total number of 1s
        nums = nums + nums  # Double the array to handle the circular array problem
        N = len(nums)
        
        left, right = 0, 0
        count = 0
        
        # Initialize the first window
        for i in range(numOnes):
            if nums[i] == 1:
                count += 1
        maxOnesInWindow = count

        # Slide the window over the array
        for right in range(numOnes, N):
            if nums[right] == 1:
                count += 1
            if nums[right - numOnes] == 1:
                count -= 1
            maxOnesInWindow = max(maxOnesInWindow, count)

        return numOnes - maxOnesInWindow