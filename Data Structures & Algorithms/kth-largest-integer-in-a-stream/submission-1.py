
import heapq

class KthLargest:

    k_largest : int
    max_heap : list = []

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = []
        heapq.heapify(self.max_heap) 
        for num in nums:
            heapq.heappush(self.max_heap, -num) 
        self.k_largest = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val) #remember to flip the values cus min heap by default in python
        popped = []
        counter = 0

        print(self.max_heap)
        
        while counter < self.k_largest:
            top = heapq.heappop(self.max_heap)
            popped.append(top)
            counter += 1

        while len(popped) > 0: #have to add the values back
            heapq.heappush(self.max_heap, popped.pop())
        
        return -top

        """
        3 3 3 2 1
        """
        
