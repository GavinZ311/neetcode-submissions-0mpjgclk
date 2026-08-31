class Solution:
    def tribonacci(self, n: int) -> int:
        
        def td(n, memo: None):

            if memo is None:
                memo = {}

            if n == 0:
                return 0

            if n == 1:
                return 1
            
            if n == 2:
                return 1

            if n in memo:
                return memo[n]
            
            memo[n] = td(n-1, memo) + td(n-2, memo) + td(n-3, memo)
            return memo[n]
        
        return td(n, None)
