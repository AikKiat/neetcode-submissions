from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Array of integers candidates, containing duplicates. Only able to choose from this list.
        Return a list of uniqur combinations of candidates, chosen numbers sum to target.
        Each element chosen at once only.

        2 2 4 6 1 5 9
        0 1 2 3 5 6 7

        [2]
        |
        [2,2]  [2,4]
        |
        [2,2,4]   [2,4,6]
        |
        correct    cannot
        |go back to [2,2] --> pick [2,4] --> results in right branch --> go back again (pop) to [2] --> pick 6 --> [2,6] --> correct! --> then pop again --> [2] --> [2,1] --> havent reached target or more than target (still < target) --> [2,1,5] correct! (again, add to global list) --> pop again --> this time pop just one level (always return back up to the precedent level) --> [2,1] --> add 9 --> [2,1,9] --> cannot --> cus for loop is done, pop() --> [2,1] --> pop() --> [2,5]...and the sequence continues.
        """

        candidates.sort()

        def recurse_and_return(index, subset, total):
            if total == target:
                result.append(subset[:])
                return

            elif total > target or index >= len(candidates): #cannot recurse further anymore, as we cannot create a new for loop iteration starting from this index to elements beyond it. Since we have already run to the end of the list
                return


            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue #we must go past the index first, and then once we are past it, we are exploring all the possible branches under this chosen, given root which is represented by the element at index. So, lets say after the element (index) = 9, we have 2,2,4. EACH OF THESE each indices represent possible branch paths. However, would the two 2s give the overall same extended subset? Yes! --> [9,2] and [9,2] --> hence, we should skip values already found, and basically skip the next 2 after accounting for the first 2. --> and sorting allows us to do this simple check. Because after sorting we can be absolutely sure that for a given element, any element less than or equal to it has already been processed.
                
                subset.append(candidates[i])
                recurse_and_return(i+1, subset, total+candidates[i])
                if len(subset) > 0:
                    subset.pop(-1)
                

        
        result = []
        recurse_and_return(0,[],0)

        return result
        