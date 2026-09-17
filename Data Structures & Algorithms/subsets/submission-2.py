class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
        1 2 3
        subset based on the length

        1 -> [1]
        1,2 -> [1, [1,2]]
        return, pop 2
        1,3 -> [1,[1,2],[1,3]]
        return pop 3
        return pop 1
        2 -> [1,[1,2],[1,3],2]
        ...
        """

        result = []
        def backtrack(subset, index):
            if index == len(nums):
                result.append(subset[:]) #we must append a new copy of subset everytime, because if we just append subset itself, we are appending the same object each time to result. Since the pointer to subset remains on this same object, everytime we modify subset we also modify the shit thing stored in result as well!!!!! Because it is 2 pointers to the same object.
                return

            result.append(subset[:])

            for i in range(index,len(nums)):
                
                subset.append(nums[i])
                backtrack(subset, i+1)
                subset.pop(-1)

                


        backtrack([],0)

        return result

        """
        Time Complexity:
        O(n!)
        Space(O(n!))
        """

        """
        f([],0) -> f([1],1)
        []         [], [1]
        """

        """
        fn([],0)
        fn([1],1) 
        [1],[1,2]
            fn([1,2],1) ---------> fn([1,3],2)
            {[1],[1,2]},[1,2,3]     {1, 1,2 1,2,3 1,3}
                    fn([1,2,3],2)
                    {1 1,2 1,2,3}
        """
            

        