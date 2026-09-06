class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Q: What is the point of using a list?
        dp = [amount + 1] * (amount + 1)
        #A: dp[i] = # of coins needed to make i. Therefore, assuming the smallest unit is 1, you'll need
        # amount + 1 amount of 1s to make amount + 1

        #Q: Why does the len of dp have to be amount + 1?
        #

        #Q: What is the point of doing dp[0] = 0??
        dp[0] = 0
        #A: 0 amount of coins is needed to make 0

        #Q: Why do we use a for loop from 1 to amount?
        for a in range(1, amount+1):
        #A: We want to calculate the # of coins needed from 1 all the way to amount

            for c in coins:
                if a - c >= 0:
        #Q: What is the point of dp[a] = ??
                    dp[a] = min(dp[a], 1+dp[a-c])

        return dp[amount] if dp[amount] != amount + 1 else -1