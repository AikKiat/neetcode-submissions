class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        The number of n denotes how many parentheses we should have at one side.
        given n = 3:
        (((
        or 
        ())
        or 
        ()(
        or
        ....

        1. We can use backtracking to generate all possible parentheses
        2. Then run valid parentheses check? (Stack approach)

        n = 1 --> *2 = 2
        )

        CURRENT: Brute force, least optimal as we generate all possible parenthesis and then check later. If we do the standard valid parenthesis check like the commented out block below, then we will TLE.

        """

        # def check_valid(parentheses : str):

        #     if len(parentheses) < 2:
        #         return False
            
        #     stack = []
        #     for p in parentheses:
        #         if p == '(':
        #             stack.append(p)

        #         else:
        #             if len(stack) == 0:
        #                 return False

        #             topmost = stack.pop(-1)
        #             if topmost != '(':
        #                 return False


        #     return True if len(stack) == 0 else False

        # def check_valid(parenthesis):
        #     #basically, check if the amount of closing braces match the opening.
        #     #and then, because of the nature of our backtracking dfs algorithm, whereby we add the opening brace first before the closing, we can be sure that closing braces definitely come after at least 1 opening brace. The problem lies in the amounts of each. However, this will not work for the standard valid parenthesis problem

        #     num_open = 0
        #     for p in parenthesis:
        #         num_open +=1 if p == '(' else -1

        #         if num_open < 0:
        #             return False
            
        #     if num_open == 0:
        #         return True

        #     return False


        # result = []
        # # seen = set()

        # def generate_all_parentheses(parenthesis): #(index, parenthesis)
        #     if len(parenthesis) == 2*n: #and parenthesis not in seen
        #         if check_valid(parenthesis):
        #             result.append(parenthesis)
        #             # seen.add(parenthesis)
        #         return

        #     ps = ['(', ')']

        #     # for i in range(index, n*2):
        #     for p in ps:
        #         generate_all_parentheses(parenthesis+p) #(index+1, parenthesis+p)


        # generate_all_parentheses("") #(0, "")

        # return result


        #Simpler and wayy faster solution --> only adding the open braces, and closed braces when neccesary, thus eliminating all wrong paths in the first place. Note that the recursion starts for the opening braces first given by recurse_and_return(parenthesis+'('), which always calls before we start recursing to add the close braces in -> recurse_and_return(parenthesis+')') --> hence, this means that we will always create parentheses that correctly start with opening braces. And:
        #-> Only add opening brace if we can add more --> less than n which denotes the length of both left half, and right half of our entire string
        #-> Only add closing brace if the current number of closing braces, is less than the opening braces so still need to achieve the balance.
        
        def recurse_and_return(parenthesis : str):
            if len(parenthesis) == 2*n:
                result.append(parenthesis)


            if parenthesis.count('(') < n: 
                recurse_and_return(parenthesis+'(')

            if parenthesis.count(')') < parenthesis.count('('): #can still add closing
                recurse_and_return(parenthesis+')')

        
        result = []
        recurse_and_return("")

        return result









        """
        n = 1*2 = 2
        2
        ()
        """






















        