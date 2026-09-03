class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if len(numbers) == 2:
            if sum(numbers) == target:
                return [1,2]

        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] > target:
                right -= 1
            elif numbers[left]+numbers[right] < target:
                left += 1

            else:
                return [left+1,right+1]
        