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

        char_hashmap = defaultdict(int)
        for char in s1:
            if char not in char_hashmap.keys():
                char_hashmap[char] = 1
            else:
                char_hashmap[char] += 1

        #iterate through s2


        l = 0
        for r in range(len(s2)):
            char_hashmap[s2[r]] -= 1 #if s2[r] is not a key, this -1 will have no effect due to nature of defaultdict. So only whenever we spot a character that is inside s1, do we decrement a legit key from the hashmap
            
            #Then, when the value associated to this particular character that exists in s1 drops below zero, we know that beforehand we have removed +1 too much. So, let's shift the left pointer forwards
            while char_hashmap[s2[r]] < 0:
                if s2[l] in s1 or s2[l] == s2[r]:
                    char_hashmap[s2[l]] += 1
                l += 1

            if len(s1) == (r - l + 1):
                return True

        return False

    """
    Rundown
    lecaabee        c
          l
          r
    """

