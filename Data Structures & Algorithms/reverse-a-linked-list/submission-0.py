# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = None
        current = head
        
        # save the rest of the list
        # reverse the current link
        # move prev forward
        # move current forward
        # [1,2,3,4]
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
