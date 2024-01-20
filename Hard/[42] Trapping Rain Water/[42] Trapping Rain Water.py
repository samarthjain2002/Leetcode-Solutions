"""
Accepted
42 [Hard]
Runtime: 144 ms, faster than 9.67% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 18.6 MB, less than 32.97% of Python3 online submissions for Trapping Rain Water
"""
class Solution:
    def trap(self, height: List[int]) -> int:

        left = []
        right = []
        left.append(height[0])
        right.append(height[len(height)-1])
        count = 0

        for i in range(1,len(height)):
            left.append(max(height[i],left[i-1]))
            j = len(height) - i - 1
            right.append(max(height[j],right[i-1]))
            
        right.reverse() 

        for i in range(0,len(height)):
            water = min(left[i],right[i]) - height[i]
            print(water)
            if water > 0:
                count += water

        return count