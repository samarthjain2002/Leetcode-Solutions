/*
Accepted
231 [Easy]
Runtime: 2 ms, faster than 11.15% of Java online submissions for Power of Two.
Memory Usage: 40.87 MB, less than 43.43% of Java online submissions for Power of Two.
 */
class Solution {
    public boolean isPowerOfTwo(int n) {
        int flag=0,fl=0;
        if(n<0)
            return false;
        if(n==1)
            flag=1;
        while(n!=0) {
            if(n%2!=0 && n!=1)
                return false;
            if(n==2)
                fl=1;
            n=n/2;
        }
        if(flag==1 || fl==1)
            return true;
        else
            return false;
    }
}