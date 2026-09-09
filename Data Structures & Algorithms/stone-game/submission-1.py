class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = [[0] * n for _ in range(n)]

        for i in range(n):
            memo[i][i] = piles[i]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                take_left = piles[l] - memo[l + 1][r]
                take_right = piles[r] - memo[l][r - 1]

                memo[l][r] = max(take_left, take_right)

        return memo[0][n - 1] > 0