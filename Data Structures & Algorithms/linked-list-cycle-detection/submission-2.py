# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # seen = set()

        # current = head

        # while current:
        #     if current in seen:
        #         return True

        #     seen.add(current)
        #     current = current.next

        # return False

        """
        Or we can use slow and fast pointers
        """

        slow = head
        fast = head

        while fast and fast.next:
            if slow == fast.next:
                return True

            slow = slow.next
            fast = fast.next.next

        return False