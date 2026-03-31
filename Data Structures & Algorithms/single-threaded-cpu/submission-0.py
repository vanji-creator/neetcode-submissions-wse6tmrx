class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i,task in enumerate(tasks):
            task.append(i)
        
        tasks.sort()
        currentTime=0
        minHeap=[]
        orderOfExecution=[]
        i=0

        while i<len(tasks) or minHeap:

            if not minHeap and currentTime<tasks[i][0]:
                currentTime=tasks[i][0]

            while i<len(tasks) and currentTime>=tasks[i][0]:
                heapq.heappush(minHeap,(tasks[i][1],tasks[i][2]))
                i+=1
            
            
            processTime,originalIndex=heapq.heappop(minHeap)
            currentTime+=processTime
            orderOfExecution.append(originalIndex)

        return orderOfExecution
                

