class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m1=m-1
        m2=n-1
        i=len(nums1)-1

        while i>=0:
            if m1<0 or m2<0:
                if m1<0:
                    nums1[i]=nums2[m2]
                    m2-=1
                    i-=1
                else:
                    nums1[i]=nums1[m1]
                    m1-=1
                    i-=1
            elif nums1[m1]>nums2[m2]:
                nums1[i]=nums1[m1]
                m1-=1
                i-=1
            else:
                nums1[i]=nums2[m2]
                m2-=1
                i-=1