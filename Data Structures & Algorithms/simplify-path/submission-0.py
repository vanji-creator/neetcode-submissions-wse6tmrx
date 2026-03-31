class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList=path.split("/")
        stack=[]
        print(pathList)
        for path in pathList:
            if path == ".." and stack:
                stack.pop()
            elif path=="." or path=="":
                continue
            elif path!="..":
                stack.append(path)

        return "/"+"/".join(stack) 