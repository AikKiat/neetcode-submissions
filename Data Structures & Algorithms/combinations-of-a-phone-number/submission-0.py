class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        
        """
        f(2,3) --> current = 2 --> a b c --> f(3) --> d e f
        for every character in f(2) --> call combinations f(3) for d e f
        -->shave off the first number, and call the function again on the rest of the phone number

        f(23)
        f(2) []
        a b c
        d e f --> ad ab ac [ad,ab,ac] 
        a a a
        b b b
        c c c

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

        if len(digits) == 0:
            return []



        def combinations(digits):
            if len(digits) == 1:
                return mapping[digits[0]]

            characters = mapping[digits[0]] #get the characters for current first digit
            result = combinations(digits[1:])

            new_result = []

            for i in range(len(result)):
                for character in characters:
                    new_result.append(character + result[i])

            return new_result

        all_combinations = combinations(digits)
        return all_combinations
















        