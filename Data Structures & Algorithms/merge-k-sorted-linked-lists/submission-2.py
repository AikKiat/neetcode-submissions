# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        1 2 4 (elements inside their own linked list will always be in non decreasing order)
        1 3 5
        3 6

        Must check --> is element 1 from ll1 > element 2 from ll2 or element3 from ll3?
        We can use a priority queue --> min heap. Add by columns. first element of all, then second element of all, etc. until we reach the end.

        Then create a new linkedlist, and pop from the queue until we are done.

        """

        min_heap = [] 
        heapq.heapify(min_heap)

        index = 0
        for linked_list in lists:
            current = linked_list
            index2 = 0
            while current:
                heapq.heappush(min_heap, (current.val, index, index2, current)) #sort by 1st value
                current = current.next

                index2 += 1

            index += 1

        #Create new listNode result
        result = ListNode()
        current = result

        while len(min_heap) > 0:
            value, index, index2, list_node = heapq.heappop(min_heap)

            current.next = list_node
            current = current.next


        return result.next
        