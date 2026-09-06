# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
      3 6 1 0
        5 9 7

      1 1 0 7


        add 2 numbers together

        all node values are >= 0 which is good.

        perform addition for each listnode at each index.

        when result less than 10, just create a new listNode with the result

        when more than 10, take result -10 , and result // 10. new ListNode with result -10 and if there is a next antecedent listNode, carry the value of result // 10 into this next subsequent listNode. Else if None, create a new ListNode to store this result. 

        Return the head of this new sum ListNode
        """
        l1_p = l1
        l2_p = l2
        carry = 0
        l_sum_head = ListNode()
        l_sum = l_sum_head
       
        while l1_p and l2_p: #this will only run for the length of the shorter of the listNodes

            l1_p_val = l1_p.val
            l2_p_val = l2_p.val
            _sum = l1_p_val + l2_p_val + carry

            carry = _sum // 10 #maximum is 18, resulting in carries always = 1
            sum_ans = _sum % 10
            
            l_sum_next = ListNode(sum_ans)

            l_sum.next = l_sum_next
            l_sum = l_sum_next

            l1_p = l1_p.next
            l2_p = l2_p.next

        #The final result of carry here, would be for a carry that could not be propogated forward because one of the nodes (or both) have come to an end.


        while l1_p:
            
            _sum = carry + l1_p.val
            
            l_sum_next = ListNode(_sum % 10)
            carry = _sum // 10
            l_sum.next = l_sum_next
            l_sum = l_sum_next

            l1_p = l1_p.next

        while l2_p:
            l_sum.next = ListNode()
            
            l_sum_next = ListNode((carry + l2_p.val) % 10)
            l_sum.next = l_sum_next
            l_sum = l_sum_next

            carry = carry + l2_p.val // 10

            l2_p = l2_p.next

        if carry > 0:
            l_sum_next = ListNode(carry)
            l_sum.next = l_sum_next
            l_sum = l_sum_next


        return l_sum_head.next


        
            

                






