class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        We can conduct BFS from the treasures themselves, and then propogate the values to all land cells. Naturally, those land cells that cannot be reached will remain as 2**31-1. And for every land cell traversed, we add it to queue in the form of (land_cell x, land_cell y, fucking distance from treasure --> which wil be closest since we do BFS --> but we have to update this for all treasure chests and finally take the minimum)

        Hence, this is reversed BFS (Similar Pacific Island Water Flow)
        """


        def bfs(queue):

            while queue:

                current = queue.pop(0)
                cur_r, cur_c = current[0]
                distance = current[1]

                if (cur_r, cur_c) in visited:
                    continue

                visited.add((cur_r, cur_c))

                directions = [(0,1),(1,0),(-1,0),(0,-1)]

                for d in directions:

                    new_r, new_c = cur_r + d[0], cur_c + d[1]

                    if (new_r, new_c) in visited:
                        continue

                    if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                        continue

                    #if we found land, or a currently traversed land..
                    if grid[new_r][new_c] != 0 and grid[new_r][new_c] != -1:
                        grid[new_r][new_c] = min(grid[new_r][new_c], distance+1)

                        queue.append(((new_r, new_c), grid[new_r][new_c]))

        ROWS = len(grid)
        COLS = len(grid[0])

        queue = []

        for r in range(ROWS):
            for c in range(COLS):
                #only perform BFS for all treasure chests
                if grid[r][c] == 0:
                    queue.append(((r,c),0))

        visited = set()
        bfs(queue)

        



