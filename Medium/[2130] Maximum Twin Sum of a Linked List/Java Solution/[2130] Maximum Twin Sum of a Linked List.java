//Accepted
//2130 [Medium]
//Runtime: 11 ms, faster than 12.92% of Java online submissions for Maximum Twin Sum of a Linked List.
//Memory Usage: 112.71 MB, less than 19.99% of Java online submissions for Maximum Twin Sum of a Linked List.
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        ListNode ptr=head;
        int sum,max=0,i,count=0;
        while(ptr!=null) {
            count++;
            ptr=ptr.next;
        }
        int n[]=new int[count];
        ptr=head;
        for(i=0;i<count;i++) {
            if(ptr!=null) {
                n[i]=ptr.val;
                ptr=ptr.next;
            }
            else
                break;
        }
        for(i=0;i<n.length/2;i++) {
            sum=n[i]+n[n.length-1-i];
            if(max<sum)
                max=sum;
        }
        return max;
    }
}