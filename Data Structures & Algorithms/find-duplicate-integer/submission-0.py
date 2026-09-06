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
        """

        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)

            else:
                return num


        