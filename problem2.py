# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jinwei = 0
        head = None
        tail = None
        head1 = l1
        head2 = l2
        while not (head1 is None and head2 is None):
            val = 0
            if head1 is not None:
                val += head1.val
                head1 = head1.next
            if head2 is not None:
                val += head2.val
                head2 = head2.next
            
            val += jinwei
            jinwei = val//10
            val = val%10
            if head is None:
                newNode = ListNode(val = val,next = None)
                head = newNode
                tail = newNode
            else:
                newNode = ListNode(val = val,next = tail.next)
                tail.next=newNode
                tail = newNode
        if jinwei > 0 :
            newNode = ListNode(val = jinwei,next = tail.next)
            tail.next=newNode
            tail = newNode
        return head
