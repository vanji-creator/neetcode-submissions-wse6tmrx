class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total=0
        for number in nums:
            total+=number
        
        if total%k !=0:
            return False
        
        target=total//k
        slots=[target]*k

        def dfs(i):
            if i==len(nums):
                return True
            seen=set()
            for j in range(k):

                if slots[j]-nums[i]<0:
                    continue
                
                if slots[j] in seen:
                    continue
                
                seen.add(slots[j])
                slots[j]-=nums[i]
                if dfs(i+1):
                    return True
                
                slots[j]+=nums[i]
                if slots[j]==target:
                    break
            return False
        
        return dfs(0)
