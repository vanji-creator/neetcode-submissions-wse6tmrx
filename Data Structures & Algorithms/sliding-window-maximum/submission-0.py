class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results=[]
        dq=deque()

        for i,num in enumerate(nums):
            while dq and nums[dq[-1]]<num:
                dq.pop()

            if dq and dq[0]==i-k:
                dq.popleft()

            dq.append(i)
            if i>=k-1:
                results.append(nums[dq[0]])
        
        return results