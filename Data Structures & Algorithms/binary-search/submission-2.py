class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            return 0 if target == nums[0] else -1


        left = 0
        right = len(nums)
        while left < right:
            middle = (left+right) // 2
            if nums[middle] < target:
                left = middle+1
            elif nums[middle] > target:
                right = middle

            else:
                return middle

        return -1