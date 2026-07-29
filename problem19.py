# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        x = dummy

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        for _ in range(length - n):
            x = x.next

        x.next = x.next.next

        return dummy.next

        
