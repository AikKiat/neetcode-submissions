class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Thoughts:

        to check if a permutation of s1 appears in s2
        > create a hashmap storing character counts in s1, and s2.
        > permutation needs to exist as a substring
        lecabee     abc
          l
            r

        lecaabee    abc
        l
        r
        > create a hashmap to store the character and freq counts of s1.
        > iterate through s2 in a single pass, via a sliding window
        """
        freq_map = {}
        for char in s1:
            if char not in freq_map.keys():
                freq_map[char] = 1

            else:
                freq_map[char] += 1


        #2 fucking cases for this fucking question. Fuck this question
        """
        1 --> we fucking got 1 shit character not in s1 in the fucking sliding window so we dump all fuck shit out since this substring is poisoned.
        2 --> we took took too much of one fucking character to now we need to shit the fuck shit l until we have JUST NICE of that shit fucking character
        """

        l = 0
        for r in range(len(s2)):
            if s2[r] not in freq_map.keys(): #first fucking case
                while l <= r: #swe want to start at a new slate, so when this while loop terminates l = r+1 --> one more character beyond this shit r character that does not appear in s2.
                    if s2[l] in freq_map.keys():
                        freq_map[s2[l]] += 1
                    l += 1

            elif s2[r] in freq_map.keys():
                freq_map[s2[r]] -= 1

                while freq_map[s2[r]] < 0:
                    if s2[l] == s2[r] or s2[l] in freq_map.keys():
                        freq_map[s2[l]] += 1

                    l += 1

            if len(s1) == (r-l+1): #only chcks out when we really never move l, and thus all stupid characters within l and r inclusive were all corr3ect.
                return True

        return False


        """
        Much betterthan the fucking previous solution.
        TiME: O(n)
        sPACE: O(1)
        """






    """
    lecaabee
        l
        r
    """
