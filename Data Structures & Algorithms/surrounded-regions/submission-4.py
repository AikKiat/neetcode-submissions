class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Basically, need to capture a surrounded region.
        > region deemed surrounded if it is connected by all the Os in top, left bottom and right (not diag) + across all four sides they surrounded by Xs. Meaning if we find a certain O, lets try to do BFS and find more Os until we cant. If we cant, and we are still within limits of the board then we have found a surrounded region and we just need to turn all these logged coordinates to Xs! 
        > if we hit the edge of the board during our BFS that means the region is not surrounded so we shall leave it, and mark all as visited so we dont ever come back to the same Os again. 
        """

        visited = set()

        found_all = []

        def bfs(r,c): #the r,c here corresponds ONLY to unvisited Os.

            queue = []

            found_os = []

            b_surrounded = True #maintains as true for now

            queue.append((r,c))

            while queue:
                
                current = queue.pop(0)

                if current in visited:
                    continue

                visited.add(current)

                curr_r, curr_c = current

                if board[curr_r][curr_c] == "O":
                    if 0 < curr_r < len(board)-1 and 0 < curr_c < len(board[0])-1:
                        found_os.append((curr_r, curr_c))
                    else:
                        b_surrounded = False

                directions = [(1,0),(0,1),(-1,0),(0,-1)]

                for d in directions:
                    new_r, new_c = curr_r + d[0], curr_c + d[1]

                    if new_r < 0 or new_r >= len(board) or new_c < 0 or new_c >= len(board[0]):
                        continue

                    if board[new_r][new_c] == "O" and (new_r, new_c) not in visited:
                        queue.append((new_r, new_c))

            

            if b_surrounded == False:
                return []

            else:
                return found_os


        def transform_to_x(surrounded_coords):
            for r, c in surrounded_coords:
                board[r][c] = "X"


        #driver
        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X":
                    continue
                if (r,c) in visited:
                    continue

                result = bfs(r,c)

                found_all.extend(result)

        #Now transform
        transform_to_x(found_all)


        """
        ["O","X","X","O","X"],
        ["X","O","O","X","O"],
        ["X","O","X","O","X"],
        ["O","X","O","O","O"],
        ["X","X","O","X","O"]

        ["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","X","X"]
        ["O","X","X","X","O"],["X","X","O","X","O"]]
        """










        