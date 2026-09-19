
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        if len(nums) == 1:
            return nums[0]
        
        max_heap = []
        heapq.heapify(max_heap)

        for num in nums:
            heapq.heappush(max_heap, -num)

        while k > 0:
            top = heapq.heappop(max_heap)
            k -= 1

        return -top