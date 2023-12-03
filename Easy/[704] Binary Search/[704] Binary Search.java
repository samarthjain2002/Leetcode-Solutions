//Accepted
//704 [Easy]
//Runtime: 0 ms, faster than 100% of Java online submissions for Binary Search.
//Memory Usage: 44.7 MB, less than 38.86% of Java online submissions for Binary Search.
class Solution {
    public int search(int[] nums, int target) {
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
                mid=(low+high)/2;
                if(low>nums.length)
                    break;
            }
            else {
                high=mid-1;
                mid=(low+high)/2;
                if(high<0)
                    break;
            }
        }
        if(found)
            return mid;
        else
            return -1;
    }
}