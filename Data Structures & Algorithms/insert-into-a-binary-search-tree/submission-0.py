# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        curr=root
        while True:
            if val>curr.val:
                if not curr.right:
                    curr.right=TreeNode(val)
                    return root
                curr=curr.right
            else:
                if not curr.left:
                    curr.left=TreeNode(val)
                    return root
                curr=curr.left