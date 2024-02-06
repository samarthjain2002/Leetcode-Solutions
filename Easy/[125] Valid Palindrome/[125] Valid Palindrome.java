/*
Accepted
125 [Medium]
Runtime: 2236 ms, faster than 5.01% of Java online submissions for Valid Palindrome.
Memory Usage: 744.08 MB, less than 5.92% of Java online submissions for Valid Palindrome.
 */
class Solution {
    public boolean isPalindrome(String s) {
        String  str="",st="";
        int n=s.length();
        int flag=1;
        for(int i=0;i<n;i++)
        {
            if(s.charAt(i)>=65 && s.charAt(i)<=90)
                str=str+(char)(s.charAt(i)+32);
            else if(s.charAt(i)>=97 && s.charAt(i)<=122)
                str=str+s.charAt(i);
            else if(Character.isDigit(s.charAt(i)))
            	str=str+s.charAt(i);
        }
        int x=str.length();
        for(int i=0;i<x;i++)
        {
            st=st+str.charAt((x-1)-i);
        }
        //System.out.println(str);
        //System.out.println(st);
        for(int i=0;i<x;i++)
        {
            if(str.charAt(i)!=st.charAt(i))
                flag=0;
        }
        if(flag==1)
            return true;
        else
            return false;
    }
}