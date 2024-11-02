//Accepted
//7 [Medium]
//Runtime: 3 ms, faster than 28.55% of Java online submissions for Reverse Integer.
//Memory Usage: 40.6 MB, less than 85.20 of Java online submissions for Reverse Integer.
//Wrote the reverse code myself
class Solution {
    public int reverse(int x) {
        int y=x,c,res=0,res1=0,count=0,i,n=0;
        boolean neg=false;
        if(x<0) {
            x=x*-1;
            neg=true;
        }
        while(y!=0) {
            y=y/10;
            count++;
        }
        for(i=count;i>0;i--) {
            if(x/10==0)
                c=x;
            else
                c=x%10;
            x=x/10;
            res=(int)(res+c*Math.pow(10,i-1));
        }
        if(neg==true)
            res=res*-1;
        res1=res;
        //from stack overflow
        //https://stackoverflow.com/questions/70048738/the-32bit-range#:~:text=You%20need%20to%20check%20if%20the%20range%20is,return%200%3B%20%7D%20%7D%20return%20%28int%29n%3B%20%7D%20Share
        for(;res1 != 0;n=((n * 10) + res1 % 10),res1 /= 10) {
          if ((res1 > 0 && n > 214748364) || (res1 > 7 && n == 214748364))
            return 0;
          else if (res1 < 0 && n < -214748364 || res1 <-8 && n == -214748364)
            return 0;
        }
        return res;
    }
}