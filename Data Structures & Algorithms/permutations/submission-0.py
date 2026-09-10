class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        1 2 3
        1        2       3
      2   3     1  3    2  1
     3     2   3    1  1    2

     Basically, decision tree. We can use DFS (recursion) to traverse all branches, and return all possible permutations. Add to a global list of permutations.
        """



        result = []
        branch_result = []
        def dfs():
            if len(branch_result) == len(nums):
                result.append([num for num in branch_result])
                return

            for i in range(len(nums)):
                if nums[i] in branch_result:
                    continue
                branch_result.append(nums[i])
                dfs()
                branch_result.pop(-1)

        if len(nums) == 1:
            return [nums]

        dfs()
        return result

        """
        f(0)--> 1 --> [1] --> f(1)--> [1,2] --> [[1,2,3]]
        """
        