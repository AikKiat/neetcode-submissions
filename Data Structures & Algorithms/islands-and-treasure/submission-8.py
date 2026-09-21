class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        We can conduct BFS from the treasures themselves, and then propogate the values to all land cells. Naturally, those land cells that cannot be reached will remain as 2**31-1. And for every land cell traversed, we add it to queue in the form of (land_cell x, land_cell y, fucking distance from treasure --> which wil be closest since we do BFS --> but we have to update this for all treasure chests and finally take the minimum)

        Hence, this is reversed BFS (Similar Pacific Island Water Flow)

        Final Update: Instead of running Separate BFS for every treasure chest and updating the values, we can do ONE batch BFS with all of the treasure chests queued, and then have a global visited set. Because of the nature of BFS, every land that is first touched, will naturally have the smallest value. So the moment we touch a piece of land, we know that we do not need to update its value any longer.
        """


        def bfs(queue):

            while queue:

                current = queue.pop(0)
                cur_r, cur_c = current[0]
                distance = current[1]

                #Option (1) check inside the queue if the current is already in visited, and add it here. Then we no need to do the preliminary add to visited at the source, before BFS runs given by option 2.

                # if (cur_r, cur_c) in visited:
                #     continue

                # visited.add((cur_r, cur_c))

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

                    visited.add((new_r, new_c))

        ROWS = len(grid)
        COLS = len(grid[0])

        queue = []
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                #only perform BFS for all treasure chests
                if grid[r][c] == 0:
                    queue.append(((r,c),0))
                    visited.add((r,c)) #Option (2) add at the source

        bfs(queue)

        



