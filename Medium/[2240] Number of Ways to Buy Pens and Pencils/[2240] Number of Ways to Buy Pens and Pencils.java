//Accepted
//2240 [Medium]
//Runtime: 25 ms, faster than 66.81% of Java online submissions for Number of Ways to Buy Pens and Pencils.
//Memory Usage: 40.6 MB, less than 74.89% of Java online submissions for Number of Ways to Buy Pens and Pencils.
class Solution {
    public long waysToBuyPensPencils(int total, int cost1, int cost2) {
        int i,temp;
        long sum,finsum=0;
        if(cost1>total && cost2>total)
            return 1;
        if(cost1>total)
            return (total/cost2)+1;
        if(cost2>total)
            return (total/cost1)+1;
        for(i=0;(i*cost1)<=total;i++) {
            temp=total-(i*cost1);
            sum=temp/cost2;
            sum++;
            finsum+=sum;
        }
        return finsum;
    }
}