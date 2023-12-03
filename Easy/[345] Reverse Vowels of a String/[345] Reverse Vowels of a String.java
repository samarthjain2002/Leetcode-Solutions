//Accepted
//345 [Easy]
//Runtime: 1763 ms, faster than 5.03% of Java online submissions for Reverse Vowels of a String.
//Memory Usage: 576.6 MB, less than 5.08% of Java online submissions for Reverse Vowels of a String.
class Solution {
    public String reverseVowels(String s) {
        int i,n=s.length(),count=0;
        char a[]=new char[n];
        for(i=0;i<n;i++)
            a[i]=s.charAt(i);
        for(i=0;i<n;i++) {
            if(a[i]=='a' || a[i]=='e' || a[i]=='i' || a[i]=='o' || a[i]=='u' || a[i]=='A' || a[i]=='E' || a[i]=='I' || a[i]=='O' || a[i]=='U')
                count++;
        }
        char v[]=new char[count],r[]=new char[count];
        int j=0,k=0,l=0;
        for(i=0;i<n;i++) {
            if(a[i]=='a' || a[i]=='e' || a[i]=='i' || a[i]=='o' || a[i]=='u' || a[i]=='A' || a[i]=='E' || a[i]=='I' || a[i]=='O' || a[i]=='U') {
                v[j]=a[i];
                j++;
            }
        }
        for(i=v.length-1;i>=0;i--) {
            r[k]=v[i];
            k++;
        }
        for(i=0;i<n;i++) {
            if(a[i]=='a' || a[i]=='e' || a[i]=='i' || a[i]=='o' || a[i]=='u' || a[i]=='A' || a[i]=='E' || a[i]=='I' || a[i]=='O' || a[i]=='U') {
                a[i]=r[l];
                l++;
            }
        }
        s="";
        for(i=0;i<n;i++)
            s=s+a[i];
        return s;
    }
}