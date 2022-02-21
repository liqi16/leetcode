# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        start = ListNode(-1)
        head3 = start

        while not (head1 is None and head2 is None):

            if head1 is None:
                head3.next = head2
                head2 = head2.next
                
            
            elif head2 is None:
                head3.next = head1
                head1 = head1.next
            
            else:
                a = head1.val
                b = head2.val
                if a <= b:
                    head3.next = head1
                    head1 = head1.next
                else:
                    head3.next = head2
                    head2 = head2.next
            
            head3 = head3.next

        return start.next
        
