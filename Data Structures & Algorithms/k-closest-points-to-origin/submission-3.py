import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lists = []
        points = [(x**2 + y**2, [x,y]) for x,y in points]
        heapq.heapify(points)
        for i in range(k):
            lists.append(heapq.heappop(points)[1])
        return lists