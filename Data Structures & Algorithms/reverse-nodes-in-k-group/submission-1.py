# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        So, we have to revers first k, next k, so on so forth. Leave tail end of num elements < k untouched.

        Thoughts:

        > use reverse linked list function? up till the k index...
        > basically iterate in groups of k...

        counter = 0
        current = head
        for current_bound in range(k, linkedlistlength, k):
            #jump in increments of k
            counter = 0
            #cannot create a new list and also modify vals. So need to reverse in-place
            while current:
                if counter == current_bound:
                    break

                #Reverse linked list formulae:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

                #increment counter
                counter += 1
        """




        #1 get linkedlist length first

        n = 0 #1 to simulate list lengths
        current = head
        while current:
            n += 1
            current = current.next

        offset = 0
        current = head
        starting_node = head
        first_node_prev_group_org = starting_node
        while n - offset >= k: # we just reverse all k groups
            #one offset group
            counter = 0
            window_prev = None
            
            while current and counter < k:
                next_node = current.next
                current.next = window_prev
                window_prev = current
                current = next_node

                counter += 1

            if offset == 0:
                head = window_prev #set the head to be the current last node of the first k window, which when reversed becomes the first node

            else:
                first_node_prev_group_org.next = window_prev #the first of the original unreversed prev group, is now the last node in the reversed form. SO we need to point this to the last node of the next group (when it wasnt reversed yet) --> which is now reversed to be the first node of this next group.

            first_node_prev_group_org = starting_node

            starting_node.next = current #current is now at the starting element of the next k window, unreversed.

            
            starting_node = current #thats why we point starting node here as well, to mark this as the point where =first_node_prev_group_org.

            offset += k


        return head


    """
    1 2 3 4 5 6

    """

                

        
        