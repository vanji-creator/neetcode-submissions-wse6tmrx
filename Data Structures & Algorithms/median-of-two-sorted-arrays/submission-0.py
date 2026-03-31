class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        
        m,n=len(nums1),len(nums2)
        total_left=(m+n+1)//2

        left,right=0,m
        while left<=right:
            i=(left+right)//2
            j=total_left-i

            maxLefti=float("-inf") if i==0 else nums1[i-1]
            minRighti=float("inf") if i==m else nums1[i]
            maxLeftj=float("-inf") if j==0 else nums2[j-1]
            minRightj=float("inf") if j==n else nums2[j]

            if maxLefti<=minRightj and maxLeftj<=minRighti:
                if (m+n)%2:
                    return max(maxLefti,maxLeftj)
                else:
                    return (max(maxLefti,maxLeftj)+min(minRighti,minRightj))/2
            elif maxLefti>minRightj:
                right=i-1
            else:
                left=i+1