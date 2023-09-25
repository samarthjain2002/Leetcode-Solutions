//Accepted
//999 [Easy]
//Runtime: 0 ms, faster than 100% of Java online submissions for Available Captures for Rook.
//Memory Usage: 40.2 MB, less than 25.61% of Java online submissions for Available Captures for Rook.
class Solution {
    public int numRookCaptures(char[][] board) {
        int rowPos=0,colPos=0,count=0;
        for(int i=0;i<8;i++) {
            for(int j=0;j<8;j++) {
                if(board[i][j]=='R') {
                    rowPos=i;
                    colPos=j;
                }
            }
        }
        //Rook moving up
        if(rowPos!=0) {
            for(int i=rowPos-1;i>=0;i--) {
                if(board[i][colPos]=='B')
                    break;
                if(board[i][colPos]=='p') {
                    count++;
                    break;
                }
            }
        }
        //Rook moving right
        if(colPos!=7) {
            for(int i=colPos+1;i<=7;i++) {
                if(board[rowPos][i]=='B')
                    break;
                if(board[rowPos][i]=='p') {
                    count++;
                    break;
                }
            }
        }
        //Rook moving down
        if(rowPos!=7) {
            for(int i=rowPos+1;i<=7;i++) {
                if(board[i][colPos]=='B')
                    break;
                if(board[i][colPos]=='p') {
                    count++;
                    break;
                }
            }
        }
        //Rook moving left
        if(colPos!=0) {
            for(int i=colPos-1;i>=0;i--) {
                if(board[rowPos][i]=='B')
                    break;
                if(board[rowPos][i]=='p') {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}