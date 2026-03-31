# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        ans=[]
        if not root:
            return ans
        
        while queue:
            current_list=[]
            level_length=len(queue)

            for i in range(level_length):
                node=queue.popleft()
                current_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(current_list)
        
        return ans