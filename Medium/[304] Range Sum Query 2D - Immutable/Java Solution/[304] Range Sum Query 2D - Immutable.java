/*
Accepted
304 [Medium]
Runtime: 1592 ms, faster than 5.20% of Java online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 65.10 MB, less than 63.51% of Java online submissions for Range Sum Query 2D - Immutable.
 */
class NumMatrix {
    protected int matrix[][];
    public NumMatrix(int[][] matrix) {
        this.matrix = matrix;
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for(int i = row1; i <= row2; i++)
            for(int j = col1; j <= col2; j++)
                sum += this.matrix[i][j];
        return sum;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */