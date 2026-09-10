class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        
        """
        > backtracking 
        34
        3
    d    e        f 
 g h i   g h i    g h i

        """

        mapping = {
            '2':["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],
            '7':["p","q","r","s"],
            '8':["t","u","v"],
            '9':["w","x","y","z"]
        }

        chosen_letters = []
        combinations = []

        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(chosen_letters))
                return
                

            current_digit = digits[index]
            characters = mapping[current_digit]

            for character in characters:
                chosen_letters.append(character)
                backtrack(index+1)
                chosen_letters.pop(-1)

            

        if len(digits) > 0:
            backtrack(0)
            return combinations

        else:
            return []


    """
    d         e           f
    [d]
    g h i
    """

        
                

            

            

            
















        