/*
Accepted
303 [Easy]
Runtime: 54 ms, faster than 58.18% of Java online submissions for Range Sum Query - Immutable.
Memory Usage: 16.76 MB, less than 75.11% of Java online submissions for Range Sum Query - Immutable.
*/
class NumArray {
    private int[] nums;
    public NumArray(int[] nums) {
        this.nums = nums;
    }
    
    public int sumRange(int left, int right) {
        int sum = 0;
        for(int i = left; i <= right; i ++)
            sum += this.nums[i];
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */