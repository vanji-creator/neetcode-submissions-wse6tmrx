class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #tuple with (distance,x,y)
        #heapify keys of the map
        #to heapify with exactly k closest points, maintain min heap, pop k times to get root(lowest) to kth lowest as 
        #heappop always returns the lowest in min heap which is the root
        distances=[]
        for i in range(len(points)):
            distances.append((points[i][0]**2+points[i][1]**2,points[i][0],points[i][1]))
        
        heapq.heapify(distances)
        ans=[]
        for i in range(k):
            popped_distance,popped_x,popped_y=heapq.heappop(distances)
            ans.append([popped_x,popped_y])
        
        return ans