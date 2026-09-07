class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """

        leftside ---- median --- rightside

                min of pile 1's right side
        1 3 4 | 7 --> 4.5
            ^max of pile 1's left

              min of pile 2's right side
        2 6 | 7 8 9 --> 4
          ^max of pile 2's left side

        Each pile, is set to a fixed number depending on the combined length of both arrays.

        max of pile 1's left vs max of pile2's left --> get the bigger one --> call it x
        min of pile1's right vs min of pile2's right --> get the smaller one --> call it y

        if x > y, then we need to shift this value which is x to the right pile. if x comes from pile1, then increase the number of pile2's left pile. If x comes from pile2, increase the number of stuff from pile1's left pile.

        if all ok, the return median = sum of mininum of right pile (mininum of pile1's right vs minimum of pile2's right) and maximum of left pile (max of pile1's right vs max of pile2's right) -->if the length is even number.

        else, we always allocate left pile to be greater by 1. So return max of life pile.

        1 2 3 4 4 5 7 8 9


        1 3 
         2

        we know that median = both lengths / 2 
        so we can iterate until that point.

        the same number can be repeated across nums1, nums2

        """

        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2)//2] + nums2[len(nums2)//2-1]) / 2
            else:
                return nums2[len(nums2)//2]

        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1)//2] + nums1[len(nums1)//2-1]) / 2
            else:
                return nums1[len(nums1)//2]

        total_length = len(nums1) + len(nums2)

        if total_length % 2 == 0:
            left = total_length // 2

        else:
            left = total_length // 2 + 1

        l = max(0, left - len(nums2))
        r = min(len(nums1), left)
        
        middle = (l + r) // 2
        n2_length = left - middle

        while l <= r:
            middle = (l + r) // 2
            n2_length = left - middle

            #Bounds check here. MIddle always shift between l and r. range of middle is 0, to len(nums1) which is r. We set r to be len(nums1) because sometimes we will not even need any element from nums2, and the entire left pile is from nums1
            if middle == 0:
                # Nothing on left
                n1_l_max = -float('inf')
                n1_r_min = nums1[0]

            elif middle == len(nums1):
                # Nothing on right
                n1_l_max = nums1[-1]
                n1_r_min = float('inf')

            else:
                # Normal partition
                n1_l_max = nums1[middle - 1]
                n1_r_min = nums1[middle]

            if n2_length == 0:
                n2_l_max = -float('inf')
                n2_r_min = nums2[0]

            elif n2_length == len(nums2):
                n2_l_max = nums2[-1]
                n2_r_min = float('inf')

            else:
                n2_l_max = nums2[n2_length - 1]
                n2_r_min = nums2[n2_length]      


            if n1_l_max > n2_r_min:
                r = middle - 1 #all other numbers at current middle position in nums1, coupled with subsequent numbers, are all too large to be put inside the left pile

            elif n2_l_max > n1_r_min:
                # we need more numbers form nums1
                l = middle + 1

            else:
                if total_length % 2 == 0:
                    return (max(n1_l_max, n2_l_max) + min(n1_r_min, n2_r_min)) / 2

                else:
                    return max(n1_l_max, n2_l_max) #because we set the left pile to be 1 index larger. So the median lies here for odd numbered lists.