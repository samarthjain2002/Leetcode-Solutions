"""
Accepted
303 [Easy]
Runtime: 2097 ms, faster than 15.99% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 20.80 MB, less than 6.29% of Python3 online submissions for Range Sum Query - Immutable.
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)