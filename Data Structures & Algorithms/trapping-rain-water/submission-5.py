class Solution:
    def trap(self, height: List[int]) -> int:
        """
        array of numbers > 0. elevation map. each height[i] == height of bar, width 1.

        return total amt water that can be trapped inside this map.

        always left, right bounds.

        think of adding rain water as stacking a block. If we stack one more block it means adding a block on top of a current height, and bounded by the minimum of left, right boundaries
        --> for a given index, always bounded by the largest of the heights to the left, and the largest of the heights to the right. The min of these 2 --> minimum bounds above which we cannot add anymore.

        --> keep track of these 2 vals, for every index.


              |       |
          |   |       | |
          |   | |   | | | |
        0 2 0 3 1 0 1 3 2 1
    l   0 0 2 2 2 2 2 2 3 3
    r   3 3 3 3 3 3 3 2 1 1
        --> min(l,r) - height[i] --> < 0 cannot add to total count. > 0 add to count. JUst floor it at 0.

        Edge case: if the length is < 2: (to trap need >= 3 length)
        return 0
        """


        # #Edge case:
        # if len(height) < 3:
        #     return 0

        # l = [0] * len(height)
        # l[0] = height[0]
        # r = [0] * len(height)
        # r[-1] = height[-1]

        # #accumulate l and r now

        # for i in range(1,len(height)):
        #     if height[i] > l[i-1]:
        #         l[i] = height[i]
        #     else:
        #         l[i] = l[i-1]

        # for i in range(len(height)-2, -1, -1):
        #     if height[i] > r[i+1]:
        #         r[i] = height[i]
        #     else:
        #         r[i] = r[i+1]

        # #now calculate total rainwater blocks we can stack

        # count = 0
        # for i in range(len(height)):
        #     count += max(min(l[i], r[i]) - height[i], 0) #cap the lower bound to be 0


        # return count

        """
        Time Complexity: O(n)
        Space Complexity: O(n)

        However, is there a solution with better space?


              |       |   
          |   |       | | 
          |   | |   | | | |
        0 2 0 3 1 0 1 3 2 1
              l
                r
        """

        #Edge case:
        if len(height) < 3:
            return 0

        l = [0] * len(height)
        l[0] = height[0]
        r = [0] * len(height)
        r[-1] = height[-1]

        l = 0
        r = 1

        count = 0

        while l <= r and r < len(height) and l < len(height):

            if height[l] == 0:
                l += 1

            if r == l:
                r += 1

            #now, if we hit a wall at l that is non-zero given the above, lets  check blocks indexed at r. keep track of a preliminary count. While we have not hit a block height at r that is greater than or equal to the bounding wall indexed at l now, we continue to add (wall height at l - block height at r), to this preliminary count
            
            preliminary_count = 0
            max_right = 0
            while r < len(height) and height[r] < height[l]:
                preliminary_count += (height[l] - height[r])
                if height[r] > max_right:
                    max_right = height[r]
                r += 1 #continue to shift r

            if r == len(height):
                height[l] = max_right
                r = l+1
                continue
            
            if height[r] >= height[l]:
                l = r
                r += 1
            
            count += preliminary_count

        return count


    """
    0,1,0,2,1,0,1,3,2,1,2,1
                  l
                      r
    p=4, c=5
    """



        