# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(-1)
        smallhead = small
        big = ListNode(-1)
        bighead = big
        while head is not None:
            if head.val < x:
                smallhead.next = head
                head = head.next #***
                smallhead = smallhead.next
                smallhead.next = None #***
            else:
                bighead.next = head
                head = head.next #***
                bighead = bighead.next
                bighead.next = None #***
            
        smallhead.next = big.next
        return small.next
