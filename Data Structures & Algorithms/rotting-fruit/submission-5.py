class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        if fresh fruit is horizontally, vertically adjacent --> side by side, then also becomes rotten. Like BFS, virus.

        > Find all rotton fruits, and then use bfs from these rotton fruits to corrupt all fresh fruits. The moment there are no more fresh fruits remaining (queue is 0 length), return.
        """


        visited = set()

        def bfs(queue):

            minutes = 0

            #at the start, the queue will contain all rotten fruits.
            while queue:
                
                for i in range(len(queue)):
                    curr_r, curr_c = queue.pop(0)

                    directions = [(1,0), (-1,0),(0,1), (0,-1)]

                    for d in directions:
                        new_r, new_c = curr_r + d[0], curr_c + d[1]

                        if (new_r, new_c) in visited:
                            continue

                        if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                            continue

                        #only when we find a fresh fruit...
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
                            queue.append((new_r, new_c))

                        visited.add((new_r,new_c))

                if len(queue) == 0:
                    break

                minutes += 1 #we have to add the minutes, based on the number of levels of BFS traversal.
            return minutes


        
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = []
        
        for r in range(ROWS):
            for c in range(COLS):
                #add all rotten fruits to queue first
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))

        minutes = bfs(queue)


        #did cover some ground, but failed to convert all ultimately
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] not in visited and grid[r][c] == 1:
                    return -1


        return minutes

            



        