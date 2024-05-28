# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, the depth is 0
        if root is None:
            return 0
        
        # Base case: if the node is a leaf (no children), the depth is 1
        if root.left is None and root.right is None:
            return 1
        
        # Recursive case: calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The maximum depth is 1 plus the greater of the depths of the left and right subtrees
        return 1 + max(left_depth, right_depth)
