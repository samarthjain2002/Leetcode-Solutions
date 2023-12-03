//Accepted
//35 [Easy]
//Runtime: 0 ms, faster than 100% of Java online submissions for Search Insert Position.
//Memory Usage: 43.5 MB, less than 26.5% of Java online submissions for Search Insert Position.
class Solution {
    public int searchInsert(int[] nums, int target) {
        boolean found=false;
        int low=0,high=nums.length-1,mid=(low+high)/2;
        while(!(found)) {
            if(nums[mid]==target) {
                found=true;
                break;
            }
            if(low==high)
                break;
            if(target>nums[mid]) {
                low=mid+1;
                if(high<low)
                    return mid;
                mid=(low+high)/2;
                if(low>nums.length)
                    break;
            }
            else {
                high=mid-1;
                if(high<low)
                    return mid;
                mid=(low+high)/2;
                if(high<0)
                    break;
            }
        }
        if(found)
            return mid;
        if(target<nums[0])
            return 0;
        if(nums[mid]>target)
            return mid;
        else
            return mid+1;
    }
}