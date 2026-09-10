from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        """
        construct adjacency list, do BFS until we terminate...
        loop through the adjancecy list and do BFS..
        if we have seen visited nodes skip.
        """



        adj_list = {}
        for start, end in edges:
            if start not in adj_list.keys():
                adj_list[start] = [end]
            else:
                adj_list[start].append(end)

            if end not in adj_list.keys():
                adj_list[end] = [start]
            else:
                adj_list[end].append(start)

        visited = set()
        
        def bfs(start_node):
            queue = deque([])
            queue.append(start_node) #first element
            while len(queue) > 0:
                current = queue.popleft()

                visited.add(current)

                neighbours = adj_list[current]

                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append(neighbour)


        total_components = 0

        #because we do undirected graph, adj_list will house ALL nodes

        for node in range(0, n):
            if node in visited:
                continue
                
            if node not in adj_list.keys():
                total_components += 1
                continue

            bfs(node)
            total_components += 1

        return total_components


        """
        2---> 3
        |
        1
        """



        