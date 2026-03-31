class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        currentMin=val if not self.stack else min(val,self.stack[-1][1])
        self.stack.append([val,currentMin])
    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
