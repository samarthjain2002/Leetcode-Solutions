//Accepted
//38 [Medium]
//Runtime: 27 ms, faster than 7.95% of Java online submissions for Count and Say.
//Memory Usage: 43.3 MB, less than 7.38% of Java online submissions for Count and Say.
class Solution {
    public String countAndSay(int n) {
        if(n==1)
            return "1";
        String seq="11";
        int i,j,groups;
        for(i=0;i<n-2;i++) {
            groups=1;
            for(j=0;j<seq.length()-1;j++) {
                if(seq.charAt(j)!=seq.charAt(j+1))
                    groups++;
            }
            int ht[][]=new int[groups][2];
            int ht1=0,count=1;
            for(j=0;j<seq.length()-1;j++) {
                if(seq.charAt(j)!=seq.charAt(j+1)) {
                    ht[ht1][0]=count;
                    ht[ht1][1]=seq.charAt(j)-48;
                    ht1++;
                    count=1;
                }
                else
                    count++;
                if(j==seq.length()-2) {
                    if(seq.charAt(j)==seq.charAt(j+1)) {
                        ht[ht1][0]=count;
                        ht[ht1][1]=seq.charAt(j+1)-48;
                    }
                    else {
                        ht[ht1][0]=1;
                        ht[ht1][1]=seq.charAt(j+1)-48;
                    }
                }
            }
            seq="";
            int l,m;
            for(l=0;l<ht.length;l++) {
                for(m=0;m<2;m++) {
                    seq=seq+ht[l][m];
                }
            }
        }
        return seq;
    }
}

class Solution {
    public static void main(String[] args) {
        int n=7;
        if(n==1)
            System.out.println("11");
        String seq="11";
        int i,j,groups;
        for(i=0;i<n-2;i++) {
            groups=1;
            for(j=0;j<seq.length()-1;j++) {
                if(seq.charAt(j)!=seq.charAt(j+1))
                    groups++;
            }
            int ht[][]=new int[groups][2];
            int ht1=0,count=1;
            for(j=0;j<seq.length()-1;j++) {
                if(seq.charAt(j)!=seq.charAt(j+1)) {
                    ht[ht1][0]=count;
                    ht[ht1][1]=seq.charAt(j)-48;
                    ht1++;
                    count=1;
                }
                else
                    count++;
                if(j==seq.length()-2) {
                    if(seq.charAt(j)==seq.charAt(j+1)) {
                        ht[ht1][0]=count;
                        ht[ht1][1]=seq.charAt(j+1)-48;
                    }
                    else {
                        ht[ht1][0]=1;
                        ht[ht1][1]=seq.charAt(j+1)-48;
                    }
                }
            }
            seq="";
            int l,m;
            for(l=0;l<ht.length;l++) {
                for(m=0;m<2;m++) {
                    seq=seq+ht[l][m];
                }
            }
        }
        System.out.println(seq);
    }
}