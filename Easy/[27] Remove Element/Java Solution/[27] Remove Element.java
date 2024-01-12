/*
Accepted
27 [Easy]
Runtime: 0 ms, faster than 100.00% of Java online submissions for Remove Element.
Memory Usage: 42.52 MB, less than 5.78% of Java online submissions for Remove Element.
 */
class Solution {
    public int removeElement(int[] nums, int val) {
        int count=0,a[]=new int[nums.length];
        for(int i=0;i<nums.length;i++) {
            if(nums[i]==val)
                nums[i]=200;
        }
        for(int i=0;i<nums.length;i++) {
            if(nums[i]!=200) {
                a[count]=nums[i];
                count++;
            }
        }
        for(int i=count;i<nums.length;i++)
            a[i]=200;
        for(int i=0;i<nums.length;i++) 
            nums[i]=a[i];
        return count;
    }
}