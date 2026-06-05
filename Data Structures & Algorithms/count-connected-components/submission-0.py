class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #i want parent initially to point at itself for each node
        parent=[i for i in range(n)]
        count=n
        def find(a):
            if parent[a]==a:
                return a
            return find(parent[a])
        
            
        for edge in edges:
            a,b=edge
            roota=find(a)
            rootb=find(b)
            if roota==rootb:
                continue
            parent[roota]=rootb
            count-=1
        
        return count