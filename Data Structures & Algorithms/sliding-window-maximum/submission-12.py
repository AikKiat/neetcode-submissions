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
        
        """


        # left = 0
        # result = []
        # array = []
        # heapq.heapify(array)
        # for right in range(len(nums)):
        #     heapq.heappush(array,(-nums[right], right))

        #     while array[0][1] < (right - k)+1:
        #         heapq.heappop(array) #remove all previous stale elements from the heap whenever we insert a new element inside. This comes as when we do our check, stale elements may still be present and be at the top of the heap despite already bring out of the window.


        #     if right - left + 1 > k:
        #         left += 1

        #     if right - left + 1 == k:
        #         result.append(-array[0][0]) #append the max

        
        # return result

        q = deque()      # stores indices
        result = []

        for i in range(len(nums)):

            # 1. Remove indices that are outside the current window
            while q and q[0] <= i - k:
                q.popleft()

            # 2. Remove smaller values from the back
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            # 3. Add current index
            q.append(i)

            # 4. Once the first full window exists, record max
            if i >= k - 1:
                result.append(nums[q[0]])

        return result


        """
        rundown
        1 2 1 0 4 2 6
              l   r
        -6
        -4
        -2
        -1
        -1
        [2,2,4]


        4 5 6 1 2 3
            l 

        6
        5
        4,0
        6 6 6 3
        """



        