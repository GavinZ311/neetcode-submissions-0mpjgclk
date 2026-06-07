import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lists = []
        heap = [[x**2 + y**2, x,y] for x,y in points]
        heapq.heapify(heap)
        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            lists.append([x,y])
        return lists