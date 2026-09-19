
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        first, calculate the damn distance of each point from the origin via the cartesian formula c^2 = a^2 + b^2 we no need to squareroot cus anyway this forms the right benchmark 
        By distance-squared basically --> squareroot v compute heavy avoid that shit

        THen add to heap as tuple (distance, [coords x and y]) and thus heapify by first element. Since answer is guaranteed to be unique, we are sure that will not have 2 coords having the same distance-squared which will screw up our heap cus become sort by second element in tuple which is the coords, will mess up.
        """

        if len(points) == 1:
            return points

        result = []


        max_heap = []

        heapq.heapify(max_heap)

        calc = lambda x, y : (x**2 + y**2)

        for point in points:
            heapq.heappush(max_heap, (calc(point[0], point[1]), point))

        while k > 0:
            point = heapq.heappop(max_heap)
            result.append(point[1])
            k -= 1

        return result
        