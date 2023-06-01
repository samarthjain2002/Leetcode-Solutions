//Accepted
//36 [Medium]
//Runtime: 11 ms, faster than 40.65% of Java online submissions for Valid Sudoku.
//Memory Usage: 46.2 MB, less than 67.80% of Java online submissions for Valid Sudoku.
class Solution {
    public boolean isValidSudoku(char[][] board) {
        int flag=1,count=0,i,j,k,f1=1,f2=1,f3=1,f4=1,f5=1,f6=1,f7=1,f8=1,f9=1;
		char a[]=new char[9];
        for(i=0;i<9;i++)		//For row elements
        {
            for(j=0;j<8;j++)
            {
                for(k=j+1;k<9;k++)
                {
                    if((board[i][j]==board[i][k]) && (board[i][j]!='.'))
                    {
                        flag=0;
                    }
                }
            }
        }
        for(i=0;i<8;i++)		//For column elements
        {
            for(j=0;j<9;j++)
            {
                for(k=i+1;k<9;k++)
                {
                    if((board[i][j]==board[k][j]) && (board[i][j]!='.'))
                    {
                        flag=0;
                    }
                }
            }
        }
		for(i=0;i<3;i++) {		//block 1
			for(j=0;j<3;j++) {
				a[count]=board[i][j];
				count++;
			}
		}
		for(i=0;i<8;i++) {
			for(j=i+1;j<9;j++) {
				if((a[i]==a[j]) && (a[i]!='.')) {
					f1=0;
				}
			}
		}
		count=0;
		for(i=0;i<3;i++) {		//block 2
			for(j=3;j<6;j++) {
				a[count]=board[i][j];
				count++;
			}
		}
		for(i=0;i<8;i++) {
			for(j=i+1;j<9;j++) {
				if((a[i]==a[j]) && (a[i]!='.')) {
					f2=0;
				}
			}
		}
		count=0;
		for(i=0;i<3;i++) {		//block 3
			for(j=6;j<9;j++) {
				a[count]=board[i][j];
				count++;
			}
		}
		for(i=0;i<8;i++) {
			for(j=i+1;j<9;j++) {
				if((a[i]==a[j]) && (a[i]!='.')) {
					f3=0;
				}
			}
		}
		count=0;
		for(i=3;i<6;i++) {		//block 4
			for(j=0;j<3;j++) {
				a[count]=board[i][j];
				count++;
			}
		}
		for(i=0;i<8;i++) {
			for(j=i+1;j<9;j++) {
				if((a[i]==a[j]) && (a[i]!='.')) {
					f4=0;
				}
			}
		}
		count=0;
		for(i=3;i<6;i++) {		//block 5
			for(j=3;j<6;j++) {
				a[count]=board[i][j];
				count++;
			}
		}
		for(i=0;i<8;i++) {
			for(j=i+1;j<9;j++) {
				if((a[i]==a[j]) && (a[i]!='.')) {
					f5=0;
				}
			}
		}
		count=0;
		for(i=3;i<6;i++) {		//block 6
			for(j=6;j<9;j++) {
				a[count]=board[i][j];
				count++;
			}
		}
		for(i=0;i<8;i++) {
			for(j=i+1;j<9;j++) {
				if((a[i]==a[j]) && (a[i]!='.')) {
					f6=0;
				}
			}
		}
		count=0;
		for(i=6;i<9;i++) {		//block 7
			for(j=0;j<3;j++) {
				a[count]=board[i][j];
				count++;
			}
		}
		for(i=0;i<8;i++) {
			for(j=i+1;j<9;j++) {
				if((a[i]==a[j]) && (a[i]!='.')) {
					f7=0;
				}
			}
		}
		count=0;
		for(i=6;i<9;i++) {		//block 8
			for(j=3;j<6;j++) {
				a[count]=board[i][j];
				count++;
			}
		}
		for(i=0;i<8;i++) {
			for(j=i+1;j<9;j++) {
				if((a[i]==a[j]) && (a[i]!='.')) {
					f8=0;
				}
			}
		}
		count=0;
		for(i=6;i<9;i++) {		//block 9
			for(j=6;j<9;j++) {
				a[count]=board[i][j];
				count++;
			}
		}
		for(i=0;i<8;i++) {
			for(j=i+1;j<9;j++) {
				if((a[i]==a[j]) && (a[i]!='.')) {
					f9=0;
				}
			}
		}
        System.out.println(flag+"\t"+f1+"\t"+f2+"\t"+f3+"\t"+f4+"\t"+f5+"\t"+f6+"\t"+f7+"\t"+f8+"\t"+f9);
		if(flag!=1 || f1!=1 || f2!=1 || f3!=1 || f4!=1 || f5!=1 || f6!=1 || f7!=1 || f8!=1 || f9!=1)
			return false;
		else
			return true;
	}
}




/*class Solution {
    public boolean isValidSudoku(char[][] board) {
        int flag=1,count=0,i,j,k;
        for(i=0;i<9;i++)
        {
            for(j=0;j<8;j++)
            {
                for(k=j+1;k<9;k++)
                {
                    if(board[i][j]==board[i][k])
                    {
                        flag=0;
                        if(board[i][j]=='.')
                            flag=1;
                    }
                }
            }
        }
        count=0;
        for(i=0;i<8;i++)
        {
            for(j=0;j<9;j++)
            {
                for(k=i+1;k<9;k++)
                {
                    if(board[i][j]==board[k][j])
                    {
                        flag=0;
                        if(board[i][j]=='.')
                            flag=1;
                    }
                }
            }
        }
		if(flag==0)
			return false;
		else
			return true;
        int i=0,j=0;
while(i!=9)
{
	while(j!=9)
	{
		for(int p=i;p<=(i+3)&&p<9;p++)
		{
			for(int q=j;q<=(j+3)&&q<9;q++)
			{
				for(int r=i+1;r<i+3&&r<9;r++)
				{
					if(board[p][q]==board[r][q])
					{
						flag=0;
						if(board[p][q]=='.')
							flag=1;
					}
				}			
			}
		}
		j=j+3;
	}
	i=i+3;
}
        if(flag==1)
            return true;
        else
            return false;
    }
}

/*for(int i=0;i<9;i+3)
{
	for(int j=0;j<9;j+3)
	{
		for(int p=i;p<=(i+3);p++)
		{
			for(int q=j;q<=(j+3);q++)
			{
				for(int r=i+1;r<i+3;r++)
				{
					if(board[p][q]==board[r][q])
					{
						flag=0;
						if(board[p][q]=='.')
							flag=1;
					}
				}			
			}
		}
	}
}

int i=0,j=0;
while(i!=9)
{
	while(j!=9)
	{
		for(int p=i;p<=(i+3);p++)
		{
			for(int q=j;q<=(j+3);q++)
			{
				for(int r=i+1;r<i+3;r++)
				{
					if(board[p][q]==board[r][q])
					{
						flag=0;
						if(board[p][q]=='.')
							flag=1;
					}
				}			
			}
		}
		j=j+3;
	}
	i=i+3;
}*/