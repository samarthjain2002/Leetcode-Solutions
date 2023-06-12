//Zigzag Conversion
//6 [Medium]
//Runtime: 151 ms, faster than 6.10% of Java online submissions for Zigzag Conversion.
//Memory Usage: 72.9 MB, less than 5.96% of Java online submissions for Zigzag Conversion.
class Solution {
    public String convert(String s, int numRows) {
        char arr[][]=new char[numRows][s.length()];
        int i=0,j=0,count=0,k,l;
        boolean yon=true;
        String str="";
        if(numRows==1)
            return s;
        for(k=0;k<arr.length;k++) {
            for(l=0;l<arr[0].length;l++) {
                arr[k][l]='$';
            }
        }
        while(true) {
            arr[i][j]=s.charAt(count);
            count++;
            System.out.println(i+"\t"+j);
            if(j%(numRows-1)==0 && i!=arr.length-1) {
                i++;
                //System.out.println("if");
            }
            else {
                //System.out.println("else");
                i--;
                j++;
            }
            if(count==s.length())
                break;
        }
        for(k=0;k<arr.length;k++) {
            for(l=0;l<arr[0].length;l++) {
                if(arr[k][l]!='$')
                    str=str+arr[k][l];
            }
        }
        for(k=0;k<arr.length;k++) {
            for(l=0;l<arr[0].length;l++) {
                System.out.print(arr[k][l]);
            }
            System.out.println();
        }
        return str;
    }
}