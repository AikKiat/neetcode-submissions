import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        """
        use a max heap, and take out 2 heaviest stones.
        Continue simulation until length of max_heap is 1
        """

        max_heap = []
        heapq.heapify(max_heap)

        #add first
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        #now smash

        while len(max_heap) > 1:
            heaviest = heapq.heappop(max_heap)
            second_heaviest = heapq.heappop(max_heap)

            if heaviest == second_heaviest:
                continue

            #else, add in the smaller shit stone
            heapq.heappush(max_heap, -abs(heaviest - second_heaviest))

        return -max_heap[0] if len(max_heap) > 0 else 0



        