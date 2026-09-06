# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        """
        Just store the next listNode to get to, continually track the previous one and get the current listNode's .next to point to this previous, and at the end current will become null after the while loop. Same goes for next_node. The last node non-null is prev, which track until the last tangile listNode. from there, it(prev's) .next would be the node that came before.
        """
        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
            
        