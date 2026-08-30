class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def top_down(idx):
            if idx <= 1:
                return 0
            if idx in memo:
                return memo[idx]

            memo[idx] = min(top_down(idx-1) + cost[idx-1], top_down(idx-2) + cost[idx-2])
            return memo[idx]
        
        return top_down(len(cost))