/*
Accepted
781 [Medium]
Runtime: 2 ms, faster than 91.49% of Python3 online submissions for Rabbits in Forest.
Memory Usage:  42.45 MB, less than 26.45% of Python3 online submissions for Rabbits in Forest.
*/
class Solution {
    public int numRabbits(int[] answers) {
        int colors[]=new int[1000],i,min=0;
        for(i=0;i<1000;i++)
            colors[i]=-1;
        for(i=0;i<answers.length;i++) {
            if(colors[answers[i]]==-1)
                colors[answers[i]]=0;
            colors[answers[i]]++;
        }
        for(i=0;i<1000;i++) {
            if(colors[i]==0)
                min++;
            if(colors[i]>0 && colors[i]<=i+1) {
                min++;
                min+=i;
            }
            if(colors[i]>0 && colors[i]>i+1) {
                while(colors[i]>i+1) {
                    min++;
                    min+=i;
                    colors[i]-=i+1;
                }
                min++;
                min+=i;
            }
        }
        return min;
    }
}