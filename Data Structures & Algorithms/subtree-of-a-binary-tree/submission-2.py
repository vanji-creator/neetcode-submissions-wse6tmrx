# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSametree(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None or root.val!=subRoot.val:
            return False
        
        return self.isSametree(root.left,subRoot.left) and self.isSametree(root.right,subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True
        if root is None:
            return False
        
        if self.isSametree(root,subRoot):
            return True
        

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        