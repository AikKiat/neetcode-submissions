class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        distinct integers list nums
        target integer target
        return list of all unique combinations (not accounting for order, only frequency) where the chosen numbers sum to target.

        nums holds distinct numbers. --> unique number per index.

        2 5 6 9

        9

        Methods:
        -> We can use backtracking to find all possible subsets of the list, and then check if the particular sum of the numbers = target.
        """


        result = []
        def dfs(current, i, total):
            if total == target:
                result.append(current[:])
                return

            elif total > target or i >= len(nums):
                return

            current.append(nums[i]) #we first add this current number to the combinations set to be considered

            dfs(current, i, total+nums[i]) #we can consider this current number in all combinations.

            current.pop(-1)

            dfs(current, i+1, total) #Or! second option is to not choose this number, and always pick others. Hence, to reach this case we of course need to pop the number first (because we first added it in in current.append(nums[i])), and for all future recursions in this tree this particular distinct number will not be included. 

        dfs([], 0, 0)

        return result

            


        