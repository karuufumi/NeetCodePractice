class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo =[-1] *(amount+1)
        def rec(n):
            if n ==0:
                return 0
            elif n <0:
                return float("inf")
            if memo[n] != -1:
                return memo[n]
            
            best = float("inf")

            for coin in coins:
                res = rec(n-coin)
                best = min(best, 1+res)
            memo[n] = best
            return best
        res = rec(amount)
        return res if res != float("inf") else -1

        