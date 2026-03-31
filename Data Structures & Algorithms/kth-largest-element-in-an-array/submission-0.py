class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted=[]
        for i in nums:
            if len(sorted)>=k:
                if sorted[0]<i:
                    heapq.heappop(sorted)
                    heapq.heappush(sorted,i)
            else:
                heapq.heappush(sorted,i)
        return sorted[0]