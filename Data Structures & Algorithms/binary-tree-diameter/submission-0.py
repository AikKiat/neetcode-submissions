# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
The maximum sum can be seen as the longest traversing distance possible?
Can be seen as maximum of sums of left height, and right height of subtrees
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        #compute height of a fuckin subtree
        def max_height(node):
            if not node:
                return 0

            return max(max_height(node.left), max_height(node.right)) +1


        def calculate_diameter(node):
            if not node:
                return 0

            subtree_left = max_height(node.left)
            subtree_right = max_height(node.right)


            diameter = subtree_left + subtree_right


            #recursively find diameter of left and right subtrees
            diameter_left = calculate_diameter(node.left)
            diameter_right = calculate_diameter(node.right)

            return max(diameter_left, diameter_right, diameter)


        result = calculate_diameter(root)

        return result




    """
    cd(root) --> l + r
    """
            


        

        



        

            
        