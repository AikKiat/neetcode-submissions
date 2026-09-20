class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        When we find land, (1) we shall expand the coverage until we can no longer find land.
        This is through BFS.

        Then, mark all these shit places as visited.

        Keep tabs on the largest piece of shit land we have covered.
        """

        visited = set()

        def bfs(r,c):

            directions = [(1,0),(-1,0),(0,-1),(0,1)]
            island_mass = 0

            visited.add((r,c))

            queue = [(r,c)]

            while len(queue) > 0: #there is more land.
                island_mass += 1
                current_row, current_col = queue.pop(0)

                for direction in directions:
                    new_row_to_go, new_col_to_go = current_row + direction[0], current_col + direction[1]
                    if (new_row_to_go, new_col_to_go) not in visited and 0 <= new_row_to_go < len(grid) and 0 <= new_col_to_go < len(grid[0]):
                        if grid[new_row_to_go][new_col_to_go] == 1:
                            queue.append((new_row_to_go, new_col_to_go))
                        
                        visited.add((new_row_to_go, new_col_to_go))


            return island_mass

        ROWS = len(grid)
        COLS = len(grid[0])

        maximum_island_mass = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited:
                    continue

                if grid[r][c] == 0:
                    visited.add((r,c))
                    continue
                
                maximum_island_mass = max(bfs(r,c), maximum_island_mass)

        return maximum_island_mass

            

        