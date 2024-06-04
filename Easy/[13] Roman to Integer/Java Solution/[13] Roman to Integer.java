/*
Accepted
3 [Easy]
Runtime: 37 ms, faster than 80.89% of Java online submissions for Roman to Integer.
Memory Usage: 45.06 MB, less than 10.75% of Java online submissions for Roman to Integer.
*/
class Solution {
    public int romanToInt(String s) {
		int i,n,integer=0;
		n=s.length();
		for(i=n-1;i>=0;i--)
		{
			if(s.charAt(i)=='I')
				integer=integer+1;
			else if(s.charAt(i)=='V')
				integer=integer+5;
			else if(s.charAt(i)=='X')
				integer=integer+10;
			else if(s.charAt(i)=='L')
				integer=integer+50;
			else if(s.charAt(i)=='C')
				integer=integer+100;
			else if(s.charAt(i)=='D')
				integer=integer+500;
			else
				integer=integer+1000;
			if(i>0)
			{
				if((s.charAt(i)=='V'||s.charAt(i)=='X')&&s.charAt(i-1)=='I')
					integer=integer-2;
				if((s.charAt(i)=='L'||s.charAt(i)=='C')&&s.charAt(i-1)=='X')
					integer=integer-20;
				if((s.charAt(i)=='D'||s.charAt(i)=='M')&&s.charAt(i-1)=='C')
					integer=integer-200;
			}   //end of if
        }       //end of for
        return integer;
    }           //end of main
}               //end of class