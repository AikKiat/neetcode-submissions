class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        rectangular island heights
        heights[r][c] --> height above sea level at coord r,c

        island borders pacific ocean, and atlantic ocean from bottom, right sides

        water can flow in 4 directions from a cell to neighbour, with height equal to or lower. Can also flow into the ocean.

        Find all cells where the water can flow from that cell into BOTH the pacific and atlantic oceans.

        > Do reverse BFS from all 4 sides, and must categorise into 2 sub categories --> Pacific set vs Atlantic set then find the intersection of both sets and return that shit
        """

        atlantic_set = set()

        pacific_set = set()

        def bfs(r,c):

            visited = set()

            possible_heights = set()

            queue = [(r,c)]

            while queue:
                current = queue.pop(0)
                cur_r, cur_c = current

                directions = [(1,0),(0,1),(-1,0),(0,-1)]

                visited.add(current)
                possible_heights.add((cur_r, cur_c))

                for d in directions:
                    new_r, new_c = cur_r + d[0], cur_c + d[1]

                    if new_r < 0 or new_r >= len(heights) or new_c < 0 or new_c >= len(heights[0]):
                        continue #bad coordinate

                    if (new_r, new_c) in visited:
                        continue


                    if heights[new_r][new_c] >= heights[cur_r][cur_c]:
                        #that means at this new coord, if we place water on top it can actually flow over to the current coord that we were initially at. This is a new inner point, yardstick to start BFS inside and extend our reach inside.

                        queue.append((new_r, new_c))

            return possible_heights


        #Driver code:
        ROWS = len(heights)
        COLS = len(heights[0])

        for r in range(ROWS):
            pacific_set.update(bfs(r, 0))
            atlantic_set.update(bfs(r, COLS-1))

        for c in range(COLS):
            pacific_set.update(bfs(0,c))
            atlantic_set.update(bfs(ROWS-1, c))

        return [[r,c] for r,c in pacific_set.intersection(atlantic_set)]


        