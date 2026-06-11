class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=n
        #since i have to start with the fact that all of them are separated
        
        parent=[i for i in range(n)]
        
        def find(node):
            if parent[node]==node:
                return node
            parent[node]=find(parent[node])
            #this is optimization, point all nodes directly at the root
            return parent[node]
        
        
        for edge in edges:
            a,b=edge
            if find(a)==find(b):
                continue
            count-=1
            parent[find(a)]=find(b)
            #making the parent of a point at parent of b which is union
        return count