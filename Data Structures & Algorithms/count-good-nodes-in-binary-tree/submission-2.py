# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Thinking:

--> use DFS and traverse to all nodes within the binary tree, as long as our traversal yields an ascending order or node values, then all are good nodes. the moment we hit a node that is smaller, then we return this entire collated list of good nodes --> in this case we just need to count, no need to state the list. So run dfs until we cover all nodes. Add each node to a visited set.


"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if not node:
                return 0

            count = 0

            if node.val >= max_so_far:
                count += 1

            new_max = max(max_so_far, node.val)

            return count + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)

            

    """
    Rundown:
    dfs(2) v={2}, count = 1
    dfs(1) v={1,2}, mistack=[1], return count
    """

        


        
            

            

            
        