class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Have to do backtracking

        1       2       3
        |
        2,  3
        |   |
        3   2

        global result

        base case:
        if length == 3, then add this to the resulting list

        f(length, curr):
        if length == 3, then add this to the resulting list

        for num in nums
            if num not in curr:
                curr appends num
                length + 1
                f(length)
                length -1

        Edge cases:
        if length is 1 then just return nums

        """  

        if len(nums) == 1:
            return [nums]


        result = []

        def backtrack_permute(curr):
            if len(curr) == len(nums):
                result.append(curr[:])

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack_permute(curr)
                    curr.pop(-1) #backtrack, remove the latest added and search again

        backtrack_permute([])

        return result

        
        """
        []
        [1]
        [1,2]
        [1,2,3] --> [[1,2,3]]
        [1,2]
        [1]
        [1,3]
        [1,3,2] --> [[1,2,3],[1,3,2]]
        """



