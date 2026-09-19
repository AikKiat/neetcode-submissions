class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        We need to create a backtracking route, where every choice is a palindrome. 
        aab
        |
        a               aa           aab
        |                |
        a      ab        b
        |                ^correct
        b --> correct
        Hence, [a,a,b] and [aa,b]

        We must check whether a given partition is a valid palindrome first, before we accept that partition and recurse down.
        """

        def check_valid(s):
            if len(s) % 2 != 0:
                middle = len(s) // 2
                for i in range(len(s) - middle):
                    if s[middle-i] != s[middle+i]:
                        return False
                return True

            else:
                middleLeft = len(s) // 2 - 1
                middleRight = len(s)// 2
                for i in range(len(s) - middleRight):
                    if s[middleLeft-i] != s[middleRight+i]:
                        return False

                return True



        """
        aab
        How to recurse:
        -> a, --> then add a? --> aa --> then add b? --> aab
        -> At each point, add the next following character and that is considered another branch
        -> after substring is for exp a --> whats left is this index (where a is) --> onwards --> ab only --> therefore --> start a for loop iteration again starting at this index position 
        --> add a? --> a --> new branch --> add b? --> ab, new branch --> if index reaches end, return... --> then pop last character, or return to state where character was not added, and then continue outer for loop iteration to next branch flow.
        """
        

        s_list = list(s)

        result = []

        def recurse_and_return(start, end, partition_set):

            if end >= len(s):
                if start == end:
                    result.append(partition_set[:])
                return


            substr = s[start: end+1]
            if check_valid(substr):
                partition_set.append(substr)
                recurse_and_return(end+1, end+1, partition_set)
                partition_set.pop(-1)
            
            recurse_and_return(start, end+1, partition_set)


        recurse_and_return(0,0,[])
        return result



        """
        aab

        f(0,...) --> f(1,a, []) --> ps=[a], f2(2,a, [a]) --> ps=[a,a], f3(3,b,[a,a,b])
                                                                       f3(3,ab,[])

        """















        