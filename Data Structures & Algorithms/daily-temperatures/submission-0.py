class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for i, temperature in enumerate(temperatures):
            while stack and temperature>stack[-1][0]:
                temp,stackInd=stack.pop()
                res[stackInd]=i-stackInd
            stack.append([temperature,i])
        
        return res