# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0
        def helper(node):
            if not node:
                return 0
            
            left=helper(node.left)
            right=helper(node.right)

            self.max_diameter=max(self.max_diameter,left+right)
            return max(left,right)+1
        
        helper(root)
        return self.max_diameter