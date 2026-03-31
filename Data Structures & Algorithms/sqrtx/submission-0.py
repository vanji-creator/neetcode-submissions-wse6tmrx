class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=0,x
        while left<=right:
            mid=left+(right-left)//2
            result=mid*mid
            if result==x:
                return mid
            elif result>x:
                right=mid-1
            else:
                left=mid+1
        return left-1