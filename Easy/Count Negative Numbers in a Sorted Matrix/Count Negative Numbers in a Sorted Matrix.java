//Accepted
//1351 [Easy]
//Runtime: 0 ms, faster than 100% of Java online submissions for Count Negative Numbers in a Sorted Matrix.
//Memory Usage: 44.4 MB, less than 18.22% of Java online submissions for Count Negative Numbers in a Sorted Matrix.
class Solution {
    public int countNegatives(int[][] grid) {
        int i=grid.length-1,j=0,count=0;
        while(!(i==0 && j==grid[0].length)) {
            if(i<0 || j==grid[0].length)
                break;
            if(grid[i][j]<0) {
                count+=grid[0].length-j;
                i--;
                continue;
            }
            if(grid[i][j]>=0) {
                j++;
                continue;
            }
        }
        return count;
    }
}