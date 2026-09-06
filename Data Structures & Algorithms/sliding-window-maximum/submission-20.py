import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Given an array, size k.
        Slides left to right
        for every iter, we get the max of the window.
        then add this max to a running list order.

        Thoughts:
        naive: Get max() of each window but this is O(k) which is bad. And we are creating a new array every time so this is bad for space and time as well
        We can add on to the window until we reach k, and once more than k (k+1) decrease from the left. if the element we decrease from the left is the maximum we need to check again if the same left exists  in the current window?

        --> maintain a max heap to get the current next max out --> after popping, do a heapify which is log(n). Building from the start is O(n)


        Update:
        Can use a queue, in below solution. O(n), O(k) space.
        
        """

        result = []
        queue = deque()  # stores index. So, we always keep track of the running maximum for the window ONLY. Not running global maximum. (INDEX wise)
        left = 0

        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop() 
                #(1) this while loop make sure that we always keep the maximum, greatest record per window, as the first in the queue. Any index holding samller elements, will get popped --> default pop is -1. Yeah so remove the latest added, with the new greater maximum. Else, just append at the back.
            queue.append(r)

            #(2) Then do cleanup here, to remove stale indices out of window
            if left > queue[0]:
                queue.popleft() 
                #(3) if the parituclar earliest entry of running maximum for the window is now smaller than the left pointer, (we store index so hence can compare directly with l)--> then this maximum is no longer valid and we need to remove it.

            if r+1 >= k:
                result.append(nums[queue[0]])
                left += 1

        return result


        """
        1 2 1 0 4 2 6
              
        
        [1,4]

        """
