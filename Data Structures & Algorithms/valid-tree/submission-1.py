class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        parent=[i for i in range(n)]
        
        def find(node):
            if parent[node]==node:
                return node
            parent[node]=find(parent[node])
            return parent[node]
        
        
        for edge in edges:
            a,b=edge
            roota=find(a)
            rootb=find(b)
            
            if roota==rootb:
                return False
            parent[roota]=parent[rootb]
        
        if len(edges)==n-1:
            return True
        else:
            return False
            
        
        