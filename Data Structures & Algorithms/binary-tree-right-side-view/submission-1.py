# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        traverse binary tree, just those viewable from the right side

        Thoughts:

        1: no other right elements blocking
        > root is definitely added
        
        function order(node):
            print(node) -> preorder (returns in order of constructing copy of tree)
            order(node.left)
            order(node.right)
        function order(node):
            order(node.left)
            print(node) -> inorder (returns in ascending order (only for BSTs))
            order(node.right)
        function order(node):
            order(node.left)
            order(node.right)
            print(node) -> postorder


        Conduct BFS on the binary tree, using Level order traversal

        Edge case:
        root is null --> can have 0 nodes..
        """

        if root is None:
            return []


        rightmost_at_each_level = [root.val]

        queue = [root]


        def get_lists():
            next_level_lst = []
            next_level_nodes_vals = []
            while len(queue) > 0:
                current = queue.pop(0)

                if current.left:
                    next_level_lst.append(current.left)
                    next_level_nodes_vals.append(current.left.val)

                if current.right:
                    next_level_lst.append(current.right)
                    next_level_nodes_vals.append(current.right.val)

            return next_level_lst, next_level_nodes_vals


        while len(queue) > 0:
            next_level_lst, next_level_nodes_vals = get_lists()
            if len(next_level_nodes_vals) > 0:
                rightmost_at_each_level.append(next_level_nodes_vals[-1])

            queue.extend(next_level_lst)


        return rightmost_at_each_level


                

                

                
















        