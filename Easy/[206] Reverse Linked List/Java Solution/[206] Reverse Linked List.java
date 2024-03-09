/*
Accepted
206 [Easy]
Runtime: 17 ms, faster than 5.36% of Java online submissions for Reverse Linked List.
Memory Usage: 42.08 MB, less than 90.70% of Java online submissions for Reverse Linked List.
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
    ListNode tail;
    public ListNode reverseList(ListNode head) {
        Solution s=new Solution();
        ListNode ptr=head;
        int count=0,i,j=0;
        while(ptr!=null) {
            count++;
            ptr=ptr.next;
        }
        int n[]=new int[count],nrev[]=new int[count];
        ptr=head;
        for(i=0;i<count;i++) {
            if(ptr!=null) {
                n[i]=ptr.val;
                ptr=ptr.next;
            }
            else
                break;
        }
        for(i=count-1;i>=0;i--) {
            nrev[j]=n[i];
            j++;
        }
        for(i=0;i<count;i++)
            tail=s.addLast(nrev[i]);
        return tail;
    }
    ListNode addLast(int ele) {
        ListNode temp=new ListNode();;
        temp.val=ele;
        temp.next=null;
        if(tail==null)
            tail=temp;
        else {
            ListNode cur=tail;
            while(cur.next!=null)
                cur=cur.next;
            cur.next=temp;
        }
        return tail;
    }
}