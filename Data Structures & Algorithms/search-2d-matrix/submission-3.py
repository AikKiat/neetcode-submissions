class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        we can perform binary search on both the row, and the column indices.
        target is greater than last row element for row a but smaller than first row element of row b, then it lies in row a.
        Pick the middle row --> if last element in this middle row is less than target, than row's top pointer comes down to this middle+1. Else, the bottom pointer goes up to middle -1.
        Once we fix the row index --> perform binary search on the columns.

        Edge case:
        if matrix is 1x1, return true if not false.
        """

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target

        top = 0 
        bot = len(matrix)-1

        while top <= bot:
            middle = (top + bot) // 2
            row_last_element = matrix[middle][-1]
            row_first_element = matrix[middle][0]

            if target > row_last_element:
                top = middle + 1

            elif target < row_first_element:
                bot = middle - 1

            elif target > row_first_element and target < row_last_element:
                #perform 2nd binary search on columns.
                left = 0
                right = len(matrix[middle]) -1
                while left <= right:
                    col_mid = (left+right) // 2
                    if matrix[middle][col_mid] < target:
                        left = col_mid + 1
                    elif matrix[middle][col_mid] > target:
                        right = col_mid -1
                    else:
                        return True

                return False

            else:
                return True
        
        return False


        