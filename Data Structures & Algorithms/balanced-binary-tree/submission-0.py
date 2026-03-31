# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced=True
        def helper(root):
            if root is None:
                return 0
            
            left_height=helper(root.left)
            right_height=helper(root.right)

            if abs(left_height-right_height)>1:
                self.isBalanced= False
            
            return 1+max(left_height,right_height)
        helper(root)
        return self.isBalanced