/*
Accepted
58 [Easy]
Runtime: 2 ms, faster than 13.54% of Java online submissions for Length of Last Word.
Memory Usage: 41.66 MB, less than 45.57% of Java online submissions for Length of Last Word.
 */
class Solution {
    public int lengthOfLastWord(String s) {
        int i,j=0,n=s.length(),count=0,count1=0,count2=0;
        for(i=0;i<n;i++) {
            if(s.charAt(i)==' ')
                count++;
            else
                break;
        }
        for(i=n-1;i>=0;i--) {
            if(s.charAt(i)==' ')
                count1++;
            else
                break;
        }
        char a[]=new char[n-(count+count1)];
        for(i=count;i!=n-count1-1;i++) {
            a[j]=s.charAt(i);
            j++;
        }
        for(i=a.length-1;i>=0;i--) {
            if(a[i]!=' ')
                count2++;
            else
                break;
        }
        return count2;
    }
}