//Accepted
//289 [Medium]
//Runtime: 0 ms, faster than 100% of Java online submissions for Game of Life.
//Memory Usage: 42.1 MB, less than 63.45% of Java online submissions for Game of Life.
class Solution {
    public void gameOfLife(int[][] board) {
        int si=board.length,sj=board[0].length;
        int n[][]=new int[si+2][sj+2],nb[][]=new int[si+2][sj+2];
        int i,j,l=0,m=0;
        for(i=1;i<board.length+1;i++) {
            for(j=1;j<board[0].length+1;j++) {
                n[i][j]=board[l][m];
                m++;
            }
            m=0;
            l++;
        }
        for(i=1;i<board.length+1;i++) {
            for(j=1;j<board[0].length+1;j++) {
                nb[i][j]=n[i][j-1]+n[i-1][j]+n[i][j+1]+n[i+1][j]+n[i-1][j-1]+n[i-1][j+1]+n[i+1][j+1]+n[i+1][j-1];
            }
        }
        l=0;m=0;
        for(i=1;i<board.length+1;i++) {
            for(j=1;j<board[0].length+1;j++) {
                if(nb[i][j]<2)
                    board[l][m]=0;
                else if(nb[i][j]>3)
                    board[l][m]=0;
                else if(board[l][m]==0 && nb[i][j]==3)
                    board[l][m]=1;
                m++;
            }
            m=0;
            l++;
        }
    }
}