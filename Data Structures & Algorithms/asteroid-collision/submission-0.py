class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1]>0 and stack[-1]+asteroid<0:
                    stack.pop()
                if stack and stack[-1]>0 and stack[-1]+asteroid==0:
                    stack.pop()
                    continue
                elif stack and stack[-1]>0 and stack[-1]+asteroid>0:
                    continue
                stack.append(asteroid)
        
        return stack