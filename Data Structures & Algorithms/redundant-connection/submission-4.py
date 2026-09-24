class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        > construct adjacency list first
        > perform DFS, and if we detect a cycle:
        1 -> 2 -> 3 -> 4
        now edge added from 4 to 1 --> 4-> 1 --> removing edge 4,1 is correct

        1 -> 2 -> 3
        edge from 3->1 --> also remove this edge and we are correct.
        > try to find a cycle. --> if a cycle is detected given a current node, and one of the neighbours, then we return this edge of [current, neighbour]

        The thing is this is an undirected graph --> so the adjancency list needs to include both source and dest. the cycle detection is done within ONE DFS traversal given a source, and it is particularly the edge from [node -> source] which we have to return
        """

        #build adjacency list

        adj_list = {}

        for edge in edges:
            source = edge[0]
            dest = edge[1]

            if source in adj_list.keys():
                adj_list[source].append(dest)

            else:
                adj_list[source] = [dest]

            if dest in adj_list.keys():
                adj_list[dest].append(source)

            else:
                adj_list[dest] = [source]


        def dfs(node, path, previous):

            path.add(node)

            neighbours = adj_list[node]
            for n in neighbours:
                if n in path:
                    #now we must check if this edge was explicitly mentioned, otherwise we are just going backwards along the same edge
                    if n == previous:
                        continue
                    elif [node, n] not in edges:
                        continue
                    else:
                        return [node,n] if [node,n] in edges else [n,node]
                        
                
                result = dfs(n, path, node)
                
                if len(result) > 0:
                    return result

            path.remove(node)

            return []

        
        final = []
        id_ = 0
        for source in adj_list.keys():
            result = dfs(source, set([]), None)
            if len(result) > 0:
                if id_ < edges.index(result, 0, len(edges)):
                    final = result
                    id_ = edges.index(result, 0, len(edges))

        return final

        """
        1 -> 2, 3
        3 -> 1, 4
        2 -> 1, 4
        4 -> 3
        """



        


            




        