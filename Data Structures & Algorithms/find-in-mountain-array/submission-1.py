class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        left,right=0,n-1
        while left<right:
            mid=(left+right)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                left=mid+1
            else:
                right=mid
        peak=right
        if target>mountainArr.get(peak):
            return -1

        left,right=0,peak
        while left<=right:
            mid=(left+right)//2
            curr=mountainArr.get(mid)
            if curr==target:
                return mid
            elif curr>target:
                right=mid-1
            else:
                left=mid+1
        
        left,right=peak,n-1
        while left<=right:
            mid=(left+right)//2
            curr=mountainArr.get(mid)
            if curr==target:
                return mid
            elif curr>target:
                left=mid+1
            else:
                right=mid-1
        return -1
        