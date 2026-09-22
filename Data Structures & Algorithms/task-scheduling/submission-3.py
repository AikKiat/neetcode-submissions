
import heapq

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        """
        we maintain a max heap of the frequency counts of tasks
        maintain a queue that stores (timestamp till task is available again, task freq count left) --> and then add this freq count back to the max heap when we pop from queue
        maintain finally a timestamp that increments with each cycle
        """

        max_heap = []
        heapq.heapify(max_heap)


        #add the frequencies
        for task, freq in Counter(tasks).items():
            heapq.heappush(max_heap, -freq)

        
        queue = []
        timestamp = 0

        while len(max_heap) > 0 or len(queue) > 0:

            timestamp += 1

            if not max_heap:
                timestamp = queue[0][0]

            else:
                freq_count = 1 + heapq.heappop(max_heap)

                if freq_count < 0: #negative cus of max heap mechanics in python
                    queue.append([timestamp + n, freq_count])

            if queue and queue[0][0] == timestamp:
                heapq.heappush(max_heap, queue.pop(0)[1])

        
        return timestamp



                


