class Solution:
    def isValid(self, s: str) -> bool:
        windowStack=[]
        open={"{":"}","[":"]","(":")"}
        for string in s:
            if string in open:
                windowStack.append(string)
            else:
                if len(windowStack)==0:
                    return False
                elif open[windowStack[-1]]==string:
                    windowStack.pop()
                else:
                    return False
        return not windowStack



