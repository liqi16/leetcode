# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        index = 1
        newnode = ListNode(-1)
        leftnode = None
        while cur is not None:

            while index >= left and index <= right:
                if index == left:
                    left_node = cur
                head = cur.next
                cur.next = newnode.next
                newnode.next = cur
                cur = head
                index += 1
            
            if index < left:
                pre = cur
                head = cur.next
                cur = head
                index +=1
            if index > right:
               pre.next = newnode.next
               left_node.next = cur
               break   

        return dummy.next

           
