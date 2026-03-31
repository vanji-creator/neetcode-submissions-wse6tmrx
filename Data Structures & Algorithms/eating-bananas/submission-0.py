def validate(piles,k,h):
    total_hours=0
    for pile in piles:
        total_hours+=math.ceil(pile/k)
    return total_hours<=h


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        ans=0
        while left<=right:
            
            mid=(left+right)//2
            if validate(piles,mid,h):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
        