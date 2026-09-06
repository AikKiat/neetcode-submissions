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


        l = 0
        for r in range(len(s2)):
            if s2[r] not in freq_map.keys():
                freq_map[s2[r]] = 0
            
            freq_map[s2[r]] -= 1

            while freq_map[s2[r]] < 0:
                if s2[l] in s1 or s2[l] == s2[r]:
                    freq_map[s2[l]] += 1
                l += 1

            if r - l + 1 == len(s1):
                return True


        return False
