class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter=collections.Counter(tasks)
        max_heap=[-count for count in counter.values()]
        cooldown_queue=collections.deque()
        heapq.heapify(max_heap)
        time=0

        while max_heap or cooldown_queue:
            time+=1

            if max_heap:
                remaining_count = heapq.heappop(max_heap)+1

                if remaining_count<0:
                    unlock_time=time+n
                    cooldown_queue.append([remaining_count,unlock_time])
            if cooldown_queue:
                if cooldown_queue[0][1]==time:
                    remaining_count,_=cooldown_queue.popleft()
                    heapq.heappush(max_heap,remaining_count)
        return time

