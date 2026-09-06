"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        """
        Thoughts:
        copy.deepcopy() each listNode first

        1st pass: build new copy, then build a hashmap of old listNode to new listNode
        """


        #Edge case: head = none
        if head == None:
            return None
        
        head_copy = Node(head.val)
        copy_pointer = head_copy
        current = head

        org_to_new = {}



        #1st pass
        while current:

            org_to_new[current] = copy_pointer

            next_org_node = current.next

            if next_org_node == None:
                copy_pointer.next = None
                current = current.next
                copy_pointer = copy_pointer.next
                continue
            
            next_new_node = Node(next_org_node.val)

            copy_pointer.next = next_new_node

            current = current.next
            copy_pointer = copy_pointer.next


        #2nd pass
        copy_pointer = head_copy
        current = head
        while current:
            random = current.random
            
            if random == None:
                copy_pointer.random = None
                copy_pointer = copy_pointer.next
                current = current.next
                continue

            random_new = org_to_new[random]
            copy_pointer.random = random_new

            copy_pointer = copy_pointer.next
            current = current.next


        return head_copy
        

        

        