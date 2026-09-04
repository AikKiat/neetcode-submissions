class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        XYYX

        We can get the maximum substring we can obtain, for every single unique character inside this string.

        AAABABB
        l
             r
        
        """

        s_list = list(s)

        if len(s_list) == 1:
            return 1

        
        character_set = set(s_list)

        global_maximum = 0

        for char in character_set:
            chosen = char
            maximum = 0
            left = 0
            count = 0
            for right in range(len(s_list)):
                if s_list[right] != chosen:
                    #replace this
                    count += 1

                while count > k:
                    if s_list[left] != chosen: #that means we have encountered one of the different characters that we previously replaced
                        count -= 1
                    left += 1
                maximum = max(maximum, right - left+1) #at this point, left is already at the right new position to start a new window, and it is not at the previous element != chosen. Because when we detected this in the while loop we subtract count then increment left --> once we increment left we do the check again in the while loop. While loop will only end if count <= k and by that time, left is correct.

            global_maximum = max(maximum, global_maximum)


        return global_maximum


    """
    Rundown:
    AAABABB
    {A,B}
         r
        l

    XYYX
    l
       r

    """
        
                    



        