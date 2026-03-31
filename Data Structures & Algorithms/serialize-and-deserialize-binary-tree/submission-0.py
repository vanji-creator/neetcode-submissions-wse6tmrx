# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans=[]
        def dfs(node):
            if not node:
                ans.append("N")
                return
            
            
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data=data.split(",")
        print(data)
        queue=collections.deque(data)
        def dfs():
            curr=queue.popleft()
            if curr=="N":
                return None
                
            node=TreeNode(int(curr))
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()

