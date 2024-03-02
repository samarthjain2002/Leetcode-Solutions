"""
Accepted
977 [Easy]
Runtime: 158 ms, faster than 50.27% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 18.49 MB, less than 93.14% of Python3 online submissions for Squares of a Sorted Array.
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left, right = 0, 0
        while right < N and nums[right] < 0:
            right += 1

        if right == 0:
            return [num** 2 for num in nums]
        elif right == N:
            return [num**2 for num in nums[::-1]]
        else:
            left = right - 1

        res = []
        while left != -1 or right != N:
            if left != -1:
                if right != N:
                    if abs(nums[left]) > abs(nums[right]):
                        res.append(nums[right] ** 2)
                        right += 1
                    else:
                        res.append(nums[left] ** 2)
                        left -= 1
                else:
                    res.append(nums[left] ** 2)
                    left -= 1
            else:
                res.append(nums[right] ** 2)
                right += 1

        return res