//Accepted
//162 [Medium]
//Runtime: 0 ms, faster than 100% of Java online submissions for Find Peak Element.
//Memory Usage: 41.7 MB, less than 88.16% of Java online submissions for Find Peak Element.
class Solution {
    public int findPeakElement(int[] nums) {
        if(nums.length==1)
            return 0;
        if(nums[0]>nums[1])
            return 0;
        if(nums[nums.length-1]>nums[nums.length-2])
            return nums.length-1;
        for(i=1;i<nums.length-1;i++) {
            if(nums[i]>nums[i-1] && nums[i]>nums[i+1])
                return i;
        }
    }
}