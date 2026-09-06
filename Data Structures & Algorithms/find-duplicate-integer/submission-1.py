class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        array of integers nums containing n+1 integers.
        each integer--> range of [1,n]

        only exactly 1 repeated integer, the rest at most once.

        [1,2,3,2,2] --> 2 repeats

        Thoughts:
        > add all seen to a set?
        > then when we spot it, flag it up immediately?
        --> O(n) space, O(n) time


        Thoughts (Optimisation)
        How to use O(1) extra space?
        We can use linked list cycles. --> Floyd Cycle Finding algorithm --> tortoise and hare algo --> using slow, fast pointers. Fast pointer travels twice speed of slow. If fast meets slow, then we have detected a cycle.
        """

        # seen = set()

        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)

        #     else:
        #         return num

        """
        Lets visualise it as such --> each index, gives another number. That number nums[i] can be the "next" of a linked list.

        1 2 3 2 2
        0 1 2 3 4

        0's next is 1
        1's next is 2
        2's next is 3
        3's next is 2
        4's next is 2
        (cycle)

        Using Floyd's algo --> fast can be: nums[nums[fast]]--> 4's next is 2, 2's next is 3 according to the element-index linkage born from this array!!!
        """


        slow = 0
        fast = 0

        n = len(nums)

        while slow < n and fast < n:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                #we have detected a cycle
                break

        slow_2 = 0

        while slow_2 < n and slow < n:
            slow = nums[slow]
            slow_2 = nums[slow_2]

            if slow_2 == slow:
                return slow


        """
        1 2 3 2 2
        s
        f
        """


        