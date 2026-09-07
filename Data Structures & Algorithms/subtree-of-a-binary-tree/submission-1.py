# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Thoughts:

        can use DFS to recurse down the root tree, and if a particular node == subroot's root node --> perform DFS to compare each left, right child.
        """

        stack = [root]

        def dfs(stack):
            while len(stack) > 0:
                node = stack.pop(-1)

                if is_subtree(node, subRoot):
                    return True

                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)
            return False
                


        def is_subtree(node, subroot_node):
            if not node and subroot_node:
                return False

            if node and not subroot_node:
                return False

            if not node and not subroot_node:
                return True

            if node.val != subroot_node.val:
                return False

            return (is_subtree(node.left, subroot_node.left) and
            is_subtree(node.right, subroot_node.right))


        #Driver code
        result = dfs(stack)

        return result




        

        