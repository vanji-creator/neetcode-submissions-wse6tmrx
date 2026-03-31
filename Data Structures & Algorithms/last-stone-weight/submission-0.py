class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-stone for stone in stones]

        heapq.heapify(stones)
        
        while len(stones)>1:
            y=heapq.heappop(stones)* -1
            x=heapq.heappop(stones)* -1

            if x!=y:
                heapq.heappush(stones,-(y-x))
        
        if len(stones)==1:
            return -(stones[0])
        
        else:
            return 0