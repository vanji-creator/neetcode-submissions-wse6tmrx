class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif self.heap[0]<val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        
        return self.heap[0]
