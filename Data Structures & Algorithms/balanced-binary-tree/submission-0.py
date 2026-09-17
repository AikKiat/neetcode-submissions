# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
we have to calculate the balance at each subtree level, and the moment we spot an imbalance, we have to return false

The thing is we can calculate the left, and right heights and then take the damn difference.
If difference > 1, then we return false.

propogate the checks up, and start from smallest subtree
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True


        if not root.left and not root.right:
            return True


        def height(node):
            #calculate the height of a given tree
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            if left_height is False or right_height is False:
                return False

            if abs(left_height - right_height) > 1:
                return False

            return max(left_height, right_height) + 1 #propogate this result back up, which is the ultimate height of the encapsulating tree (which has these 2 left and right subtrees respectively)

        if height(root) == False:
            return False
        
        return True

        