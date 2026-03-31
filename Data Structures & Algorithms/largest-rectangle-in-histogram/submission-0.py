class Solution:
        def prevSmaller(self, arr: List[int])->List[int]:
            n=len(arr)
            ans=[-1]*n
            stack=[-1]
            for i in range(n):
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if stack:
                    ans[i]=stack[-1]
                stack.append(i)
            return ans
        
        def nextSmaller(self,arr:List[int])->List[int]:
            n=len(arr)
            ans=[n]*n
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if stack:
                    ans[i]=stack[-1]
                stack.append(i)
            return ans
        def largestRectangleArea(self, heights: List[int]) -> int:
            n=len(heights)
            prevSmaller=self.prevSmaller(heights)
            nextSmaller=self.nextSmaller(heights)
            ans=0
            for i in range(n):
                left=prevSmaller[i]
                right=nextSmaller[i]
                width=right-left-1
                height=heights[i]
                ans=max(ans,width*height)
            return ans