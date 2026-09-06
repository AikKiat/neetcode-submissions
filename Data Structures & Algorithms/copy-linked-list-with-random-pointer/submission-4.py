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
        
        current = head

        org_to_new = {}



        #1st pass
        while current:

            org_to_new[current] = Node(current.val)
            current = current.next


        #2nd pass
        current = head
        head_copy = org_to_new[current]
        copy_pointer = head_copy
        while current:
            random = current.random
            
            new_random = org_to_new.get(random, None)

            copy_pointer.random = new_random
            copy_pointer.next = org_to_new.get(current.next,None)
            
            copy_pointer = copy_pointer.next
            current = current.next


        return head_copy
        

        

        