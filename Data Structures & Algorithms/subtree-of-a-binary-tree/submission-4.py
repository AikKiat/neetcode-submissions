# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # """
        # Thoughts:

        # can use DFS to recurse down the root tree, and if a particular node == subroot's root node --> perform DFS to compare each left, right child.

        # Edge cases:
        # if root and subroot are both just singular nodes, we can directly compare and check. Much faster and saves heap space
        # """

        # if not root.left and not root.right and not subRoot.left and not subRoot.right:
        #     return root.val == subRoot.val

        # stack = [root]

        # def dfs(stack):
        #     while len(stack) > 0:
        #         node = stack.pop(-1)

        #         if is_subtree(node, subRoot):
        #             return True

        #         if node.left:
        #             stack.append(node.left)

        #         if node.right:
        #             stack.append(node.right)
        #     return False
                


        # def is_subtree(node, subroot_node):
        #     if not node and subroot_node:
        #         return False

        #     if node and not subroot_node: #Ah over here, this is True ONLY if we consider the subtree to be a part of the main tree and its membership need not extend to the leaf nodes. Because basically over here we are saying that if we have covered ALL nodes in the subtree, but have not reached the leaf level of the main tree, then if we consider the above --> return True. Else, for this question bounds we are returning false.
        #         return False

        #     if not node and not subroot_node:
        #         return True

        #     if node.val != subroot_node.val:
        #         return False

        #     return (is_subtree(node.left, subroot_node.left) and
        #     is_subtree(node.right, subroot_node.right))


        # #Driver code
        # result = dfs(stack)

        # return result



        """
        PREORDER TRAVERSAL SOLUTION
        We can use preorder traversal which goes through the nodes of a tree in this order:
            parent -> left -> right.
            So for exp:
            3
        4       5
    1     2   7   8
    Order is: --> 3 -> left subtree (parent)=4 -> 1 -> 2 -> right subtree (parent)=5 -> 7 -> 8 -> END.
    Hence, we cab easily check for subtrees like this, by returning if the preorder traversal of subroot is inside the preorder traversal of the main root tree itself. Use strings to check if "inside"
        """

        #Edge case: both root and subRoot have no children and are lone tree nodes. Just check for value
        if root.left is None and root.right is None and subRoot.left is None and subRoot.right is None:
            return root.val == subRoot.val

        preorder_root = ""
        preorder_subroot = ""

        def preorder(node, preorder_string):
            if not node:
                preorder_string += "None"
                return preorder_string

            preorder_string += str(node.val)
            preorder_string = preorder(node.left, preorder_string)
            preorder_string = preorder(node.right, preorder_string)

            return preorder_string

        
        preorder_root = preorder(root, preorder_root)

        #check if the subroot only contains 1 node, then it must be a leaf node with its preorder position followed by two '-' '-':
        if subRoot.left == None and subRoot.right == None:
            if str(subRoot.val) not in preorder_root:
                return False

            return f"{subRoot.val}NoneNone" in preorder_root

        preorder_subroot = preorder(subRoot, preorder_subroot)


        return preorder_subroot in preorder_root

        """
        Time Complexity: O(N * M) (last 'in' check), where N is the number of tree nodes in root, and M is the number of tree nodes in subRoot.

        Space Complexity: O(N+M), since we are writing to a string which scales in space usage according to the length of the number of nodes, and we include the null, 'non-existent' children as well which adds additional memory usage.
        """
        




        

        