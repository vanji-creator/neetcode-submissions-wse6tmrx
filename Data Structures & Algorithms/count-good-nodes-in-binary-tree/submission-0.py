# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,currMax):
            if not node:
                return 0
            count=0
            if node.val>=currMax:
                count=1
            currMax=max(node.val,currMax)
            count+=dfs(node.left,currMax)
            count+=dfs(node.right,currMax)


            
            return count
        return dfs(root,root.val)
