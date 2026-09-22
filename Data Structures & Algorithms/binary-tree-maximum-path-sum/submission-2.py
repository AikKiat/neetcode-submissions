# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        """
        we can do DFS for a given path
        parent
        |     |
        child child
        path1 path2

        the third path can be from the left child, through the parent and down to the right child.
        However, for such a traversal we can only choose to go either left deep, or right deep.
        Therefore, the path can be: left/right branch of child resulting in maximum value --> parent --> left/right branch of right child resulting in maximum value.

        We can hence do DFS given a parent node, and return its value + the larger of the left/right branches.--> this "larger of the left/right branches" is a recursive take that extends all the way down, recursing all the way down to the leaf nodes of the tree.
        """

        if not root.left and not root.right:
            return root.val


        max_path_sum = -float('inf')

        def dfs(node):
            
            nonlocal max_path_sum

            if not node:
                return 0
            
            left_result = max(0,dfs(node.left))

            right_result = max(0,dfs(node.right))

            current_sum = node.val + left_result + right_result
            max_path_sum = max(current_sum, max_path_sum)

            #Then, only the maximum path extending DOWN from this given node --> basically for the subtrees we have recursed into from this node as the parent --> we branch off into left and right subtrees and have obtained either left path sum and right path sum. Only the maximum of the 2, can be used to represent the maximum path sum for this entire tree, and in the context of this node's ulterior parent this maximum value becomes yet again the maximum for either left / right branch. So we bubble the result right back up to the root again.

            return node.val + max(left_result, right_result)

        dfs(root)

        return max_path_sum










        
        