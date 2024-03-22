/*
Accepted
234 [Easy]
Runtime: 4 ms, faster than 82.66% of Java online submissions for Palindrome Linked List.
Memory Usage: 56.04.50 MB, less than 95.73% of Java online submissions for Palindrome Linked List.
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
    public boolean isPalindrome(ListNode head) {
        ListNode ptr=head;
        boolean flag=true;
        int count=0,i;
        while(ptr!=null) {
            count++;
            ptr=ptr.next;
        }
        ptr=head;
        int n[]=new int[count];
        for(i=0;i<count;i++) {
            if(ptr!=null) {
                n[i]=ptr.val;
                ptr=ptr.next;
            }
            else
                break;
        }
        for(i=0;i<n.length/2;i++) {
            if(n[i]!=n[n.length-1-i])
                flag=false;
        }
        return flag;
    }
}