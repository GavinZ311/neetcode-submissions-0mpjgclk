import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            firstStone = heapq.heappop(max_heap)
            secondStone = heapq.heappop(max_heap)
            result = abs(firstStone*-1 - secondStone*-1)*-1
            if result != 0:
                heapq.heappush(max_heap,result)
        max_heap.append(0)
        return abs(max_heap[0])

        