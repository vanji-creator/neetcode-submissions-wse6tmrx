# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,minVal,maxVal):
            if not node:
                return True
            
            if node.val>=maxVal:
                return False
            if node.val<=minVal:
                return False
            
            leftTree=dfs(node.left,minVal,node.val)
            rightTree=dfs(node.right,node.val,maxVal)

            return leftTree and rightTree
        return dfs(root,float("-inf"),float("inf"))