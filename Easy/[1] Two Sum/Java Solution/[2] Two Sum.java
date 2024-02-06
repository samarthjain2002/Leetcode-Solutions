/*
Accepted
1 [Easy]
Runtime: 86 ms, faster than 7.31% of Java online submissions for Two Sum.
Memory Usage: 44.91 MB, less than 28.89% of Java online submissions for Two Sum.
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n=nums.length;
        int []a=new int[2];
        for(int i=0;i<n-1;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    a[0]=i;
                    a[1]=j;
                }   //end of if
            }       //end of for
        }           //end of for
        return a;
    }               //end of twoSum
}                   //end of class