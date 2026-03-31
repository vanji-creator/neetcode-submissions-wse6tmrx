class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        waterArea=0
        left,right=0,n-1
        while left<right:
            breadth=right-left
            length=min(heights[left],heights[right])
            waterArea=max(waterArea,breadth*length)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return waterArea
        