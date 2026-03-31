class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #i can execute only if w is greater than capital of that proj
        #i check the capital list if there are any projects that i could do
        #if there are more than one project, then i do the one with most profit

        # i need a dict to store key as capital requirec and value as profit
        #i have written my first principles here

        sortedCP=[]
        for i in range(len(profits)):
            sortedCP.append((capital[i],profits[i]))
        
        sortedCP.sort()
        availableProjects=[]
        j=0
        for i in range(k):

            while j<len(sortedCP) and w>=sortedCP[j][0]:
                heapq.heappush(availableProjects,-sortedCP[j][1])
                j+=1
            
            if availableProjects:
                projectProfit = -heapq.heappop(availableProjects)
                print(projectProfit)
                w+=projectProfit
        
        return w
