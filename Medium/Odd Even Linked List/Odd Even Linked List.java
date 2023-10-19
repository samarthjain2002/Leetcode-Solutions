//Accepted
//328 [Medium]
//Runtime: 46 ms, faster than 12.34% of Java online submissions for Odd Even Linked List.
//Memory Usage: 44.9 MB, less than 32.52% of Java online submissions for Odd Even Linked List.
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
    ListNode l;
    public ListNode oddEvenList(ListNode head) {
        Solution s=new Solution();
        ListNode ptr=head;
        int count=0,k=0,i;
        while(ptr!=null) {
            count++;
            ptr=ptr.next;
        }
        ptr=head;
        int n[]=new int[count],oe[]=new int[count];
        for(i=0;i<count;i++) {
            n[i]=ptr.val;
            ptr=ptr.next;
        }
        for(i=0;i<n.length;i++) {
            if(i%2==0) {
                oe[k]=n[i];
                k++;
            }
        }
        for(i=0;i<n.length;i++) {
            if(i%2!=0) {
                oe[k]=n[i];
                k++;
            }
        }
        for(i=0;i<oe.length;i++)
            head=s.addLast(oe[i]);
        return head;
    }
    ListNode addLast(int ele) {
        ListNode temp=new ListNode();
        temp.val=ele;
        temp.next=null;
        if(l==null)
            l=temp;
        else {
            ListNode ptr=l;
            while(ptr.next!=null)
                ptr=ptr.next;
            ptr.next=temp;
        }
        return l;
    }
}