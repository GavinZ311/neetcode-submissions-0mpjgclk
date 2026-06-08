import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        Nums = [-1*x for x in nums]
        heapq.heapify(Nums)
        for i in range(k):
            num = heapq.heappop(Nums)
        return num*-1