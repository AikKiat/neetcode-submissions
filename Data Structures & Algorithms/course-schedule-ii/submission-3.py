class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Use topological sort to order the courses in terms of priority --> therefore take the most important course that all depend on, and then proceed in that decreasing order of importance

        It is impossible to finish all courses, if we have detected a cycle.
        """

        #construct adjacency list first

        adj_list = {}

        for p in prerequisites:
            dependency = p[1]
            dependent = p[0]

            if dependency in adj_list.keys():
                adj_list[dependency].append(dependent)

            else:
                adj_list[dependency] = [dependent]


        visited = set()
        result = []
        def dfs_topo(node, path):
            
            if node in path:
                return False

            if node in visited:
                return True

            if node not in adj_list.keys():
                return True

            path.add(node)

            neighbours = adj_list[node]
            for n in neighbours:
                if not dfs_topo(n, path):
                    return False

            path.remove(node)

            result.append(node)
            visited.add(node) #add after the exploration. Explore all possible branches first, before finally marking this node as visited.

            return True

        #Driver code
        for node in adj_list:
            if node not in visited:
                if not dfs_topo(node, set([])):
                    return []


        #Now pop from result and add to the final topological sort list
        dependency_order = []
        for r in range(len(result)-1, -1, -1):
            dependency_order.append(result[r])

        for course_number in range(numCourses):
            if course_number not in adj_list.keys():
                dependency_order.append(course_number)

        return dependency_order


        """
        Rundown

        0 --> 1,2
        1 --> 3
        2 --> 3
        """


            

            

            


        