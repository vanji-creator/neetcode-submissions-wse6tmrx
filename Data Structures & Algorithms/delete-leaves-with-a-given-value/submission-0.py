# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        

            
        left_subtree = self.removeLeafNodes(root.left,target)
        right_subtree = self.removeLeafNodes(root.right,target)

        root.left=left_subtree
        root.right=right_subtree
        if not root.left and not root.right:
            if root.val==target:
                return None
        return root