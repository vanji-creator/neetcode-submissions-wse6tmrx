class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #i maintain a variable which is remaining capacity
        #i first sort the input list with the from point
        #so its a perfect simulation, and then i update the remaining capacity as
        #we go through this simulation, 
        #but i also have to look for other trips which might come along the way
        #so i have to know all the from points and all the to points before simulation
        #and then i have to check where all i get trips before completing trip and check if theres
        #any space
        #let me take all the from points first and loop through it
        #also for each from point i should know the drop point and 
        #number of passengers that would get down at that point
        # first when i start from first point, i have the current remaining capacity
        #then i update it if another from point comes before dropping
        #i maintain a pointer variable which marks the distance
        #when i go to each point i check first outgoing and incoming passengers and check
        #the car will fit them, do this until the end, if no false anywhere inbtw return true
        events=[]
        for numOfPassengers,fromPoint,toPoint in trips:
            events.append((fromPoint, numOfPassengers))
            events.append((toPoint, -numOfPassengers))

        events.sort()

        currentPassengers=0
        for mileMarker,passengerChange in events:
            currentPassengers+=passengerChange

            if currentPassengers>capacity:
                return False
        
        return True
