class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverser(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1

        k= k%len(nums)
        reverser(0,len(nums)-1)
        reverser(0,k-1)
        reverser(k,len(nums)-1)