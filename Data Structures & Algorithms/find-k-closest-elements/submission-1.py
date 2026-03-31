class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left=0
        right=len(arr)-1

        while left<right:
            mid=(left+right)//2
            if arr[mid]<x:
                left=mid+1
            else:
                right=mid
        
        left_ptr=left-1
        right_ptr=left

        while k>0:
            if left_ptr<0:
                right_ptr+=1
            elif right_ptr==len(arr):
                left_ptr-=1
            elif abs(arr[left_ptr]-x) <= abs(arr[right_ptr]-x):
                left_ptr-=1
            else:
                right_ptr+=1
            k-=1
        
        return arr[left_ptr+1:right_ptr]

