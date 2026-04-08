class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer=[]
        letters={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if len(digits)==0:
            return []
        

        def dfs(start,current):
            if len(current)==len(digits):
                answer.append(current)
                return
            
                # for digit in range(len(letters[int(digits[start])])):
            for character in letters[int(digits[start])]:
                dfs(start+1,current+character)
            
        dfs(0,"")
        return answer