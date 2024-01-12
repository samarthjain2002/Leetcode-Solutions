/*
Accepted
26 [Easy]
Runtime: 401 ms, faster than 5.06% of Java online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 45.10 MB, less than 6.14% of Java online submissions for Remove Duplicates from Sorted Array.
 */
class Solution {
    public int removeDuplicates(int[] nums) {
        int n=nums.length,count=0;
        int a[]=new int[n];
        for(int i=0;i<n-1;i++) {
            for(int j=i+1;j<n;j++) {
                if(nums[i]==nums[j]) {
                    nums[j]=200;
                }
            }
        }
        for(int i=0;i<n;i++) {
            if(nums[i]!=200) {
                a[count]=nums[i];
                count++;
            }
        }
        for(int i=count;i<n;i++)
            a[i]=200;
        for(int i=0;i<n;i++)
            nums[i]=a[i];
        return count;
    }
}