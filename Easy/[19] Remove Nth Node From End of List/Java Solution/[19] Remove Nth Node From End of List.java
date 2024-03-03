/*
Accepted
19 [Easy]
Runtime: 0 ms, faster than 100.00% of Java online submissions for Remove Nth Node From End of List.
Memory Usage: 40.63 MB, less than 99.96% of Java online submissions for Remove Nth Node From End of List.
 */
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode ptr=head,cur=head;
        int count=0,i;
        while(ptr!=null) {
            count++;
            ptr=ptr.next;
        }
        ptr=head;
        int pn=count-n;
        for(i=0;i<pn;i++) {
            if(i>0)
                cur=cur.next;
            ptr=ptr.next;
        }
        if(ptr==head) {
            head=ptr.next;
            ptr.next=null;
        }
        else
            cur.next=ptr.next;
        return head;
    }
}