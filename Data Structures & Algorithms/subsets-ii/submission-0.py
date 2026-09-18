class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:



        nums.sort()

        result = []

        
        def recurse_and_return(index, subset):


            result.append(subset[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                #else, consider all branches
                subset.append(nums[i])
                recurse_and_return(i+1, subset)
                subset.pop(-1)

        recurse_and_return(0, [])

        return result


        

        