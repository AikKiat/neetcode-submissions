class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        daily temps on the ith day

        30 38 30 36 35 40 28
        0   1  2  3  4  5  6

        result[i] --> number of days after ith day, before a warmer temperature appears on a future day --> a temperature that is basically higher than the ith day, and we want to count how many days until we get this temperature.

        30 38 30 36 35 40 28
        0  1  2  3  4  5  6
        1  4  1  2  1  0  0

        1. for each i, keep a counter. 
        2. iterate until reach one day > ith day, store into results array at index i
        3. On^2 time complexity

        40,5 28,6
        30 38 30 36 35 40 28
        1  4  1  2  1  0  0

        Revised:
        so stack contains elements of (temp, index) --> whenever we encounter a new temp, we check top element in stack if it is smaller and can be resolved. If yes, continue until we hit a temperature that is greater. Then add the new (temp, index) entry to the top. 


        Edge cases:
        just 1 element

        return 0
        """

        if len(temperatures) == 1:
            return [0]


        stack = []
        results = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((temperatures[i], i))
                continue

            #ELse:
            while len(stack) > 0:
                top_element = stack[-1]
                if temperatures[i] > top_element[0]:
                    stack.pop(-1)
                    #Then resolve now, and edit entry in result being the current index of i - the associated index to this lower temperature (k), meaning that we took i - k days (rightfully so since i is i-k positions after k) to resolve this lower temperature
                    results[top_element[1]] = i - top_element[1]

                else:
                    break

            stack.append((temperatures[i], i))


        return results

        

        