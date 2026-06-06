class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent=[i for i in range(n)]

        def find(i):
            if parent[i]==i:
                return i
            parent[i]=find(parent[i])
            return parent[i]
        count=n
        for edge in edges:
            a,b=edge
            roota=find(a)
            rootb=find(b)
            if roota==rootb:
                return False
            count-=1
            parent[roota]=rootb
        
        return count==1