class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum=0
        scoreStack=[]

        for op in operations:
            if op=="+":
                temp=scoreStack.pop()
                ans=temp+scoreStack[-1]
                scoreStack.append(temp)
                scoreStack.append(ans)
                sum+=scoreStack[-1]
            elif op=="D":
                scoreStack.append(scoreStack[-1]*2)
                sum+=scoreStack[-1]
            elif op=="C":
                sum-=scoreStack[-1]
                scoreStack.pop()
            else:
                scoreStack.append(int(op))
                sum+=scoreStack[-1]
        
        return sum
        