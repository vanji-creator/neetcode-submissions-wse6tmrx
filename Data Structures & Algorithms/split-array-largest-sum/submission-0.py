def validate(nums,k,capacity):
    splits=1
    sum=0
    for number in nums:
        if sum+number>capacity:
            splits+=1
            sum=number
            continue
        sum+=number
    return splits<=k

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ans=0
        left,right=max(nums),sum(nums)
        while left<=right:
            mid=(left+right)//2
            temp=validate(nums,k,mid)
            if temp:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        
        return ans