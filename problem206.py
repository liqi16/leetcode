# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        if head is None:
            return head
        while(head.next is not None):
            nextnode = head.next
            head.next = reverse
            reverse = head
            head = nextnode
        head.next = reverse
        return head
