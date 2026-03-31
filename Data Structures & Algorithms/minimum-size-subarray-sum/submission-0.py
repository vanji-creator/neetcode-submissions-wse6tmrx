class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        minLength=len(nums)+1
        sum=0

        for right in range(len(nums)):
            sum=sum+nums[right]
            while sum>=target:
                minLength=min(minLength,right-left+1)
                sum-=nums[left]
                left+=1
        
        if minLength==len(nums)+1:
            return 0
        else:
            return minLength