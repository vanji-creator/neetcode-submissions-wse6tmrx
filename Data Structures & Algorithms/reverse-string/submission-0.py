class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        resList=s
        left = 0
        right = len(s)-1

        while left<right:
            resList[left],resList[right]=resList[right],resList[left]
            left+=1
            right-=1
        return resList

        