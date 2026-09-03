class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Edge cases:
        length 1, means only a number, due to all arithmetic expressions being valid --> hence return just this.

        in postfix notation

        1 2 + 3 * 4 -

                    ^
        operator -
        operand_left 9
        operand_right 4

        -> resulting sums go to operand_left
        -> have operand_left, operand_right, and operator

        ---> Translating to stack:

        - --> perform = 5
        4
        9
        _
        * --> 2. meet operator again, pop both 3's, lead to 9
        3
        3
        _
        + --> 1.meet operator, pop both 2 and 1. perform operation = 2+1=3

        1. when see a number add to stack
        2. when see an operator, pop the top 2 numbers from stack, perform operation, add result back to stack
        """

        stack = []

        operators = {"*": lambda x, y: x*y, "+": lambda x,y :x+y, "/":lambda x,y : int(x/y), "-":lambda x,y : x-y}
        #for minus, its always the running sum - the new right operand on top, as is case of example.
        for token in tokens:
            if token in operators:

                right = stack.pop(-1)
                left = stack.pop(-1)

                result = operators[token](left, right)
                stack.append(result)
            else:
                #token is a number
                stack.append(int(token))
        
        if isinstance(stack[0], float):
            if stack[0] - int(stack[0]) < 0.5:
                return int(stack[0])
            return int(stack[0]) + 1
        return stack[0]


        

        """
        10 6 9 3 + -11 * / * 17 + 5 +

        10 22 * 
        """






        
        