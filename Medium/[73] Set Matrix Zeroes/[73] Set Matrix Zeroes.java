//Accepted
//73 [Medium]
//Runtime: 2 ms, faster than 52.45% of Java online submissions for Set Matrix Zeroes.
//Memory Usage: 53.8 MB, less than 75.88% of Java online submissions for Set Matrix Zeroes.
class Solution {
    public void setZeroes(int[][] matrix) {
        int i,j,m=matrix.length,n=matrix[0].length,count=0;
        for(i=0;i<m;i++) {
            for(j=0;j<n;j++) {
                if(matrix[i][j]==0)
                    count++;
            }
        }
        int rec[]=new int[2*count],k=0,temp;
        for(i=0;i<m;i++) {
            for(j=0;j<n;j++) {
                if(matrix[i][j]==0) {
                    rec[k]=i;
                    k++;
                    rec[k]=j;
                    k++;
                }
            }
        }
        k=0;
        while(k<rec.length-1) {
            temp=rec[k];
            for(j=0;j<n;j++)
                matrix[temp][j]=0;
            k=k+2;
        }
        k=1;
        while(k<rec.length) {
            temp=rec[k];
            for(i=0;i<m;i++)
                matrix[i][temp]=0;
            k=k+2;
        }
    }
}