class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def solve(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float("inf")
            
            if remaining in memo:
                return memo[remaining]
            
            res = float('inf')
            for c in coins:
                res = min(res, 1+ solve(remaining-c))
            memo[remaining] = res
            return res
        
        if solve(amount) == float('inf'):
            return -1
        
        return solve(amount)


        