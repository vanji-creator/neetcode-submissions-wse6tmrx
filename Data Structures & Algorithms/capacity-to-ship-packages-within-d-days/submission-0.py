def validate(weights,days,x):
    d=1
    load=0
    for weight in weights:
        load+=weight
        if load>x:
            d+=1
            load=weight
    return d<=days


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right=max(weights),sum(weights)
        ans=right
        while left<=right:
            mid=(left+right)//2
            if validate(weights,days,mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans