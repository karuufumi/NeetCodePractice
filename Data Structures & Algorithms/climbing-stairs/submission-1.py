from functools import reduce

class Solution:
    def climbStairs(self,n: int) -> int:
        if n <= 2:
            return n

        prev2, prev1 = reduce(
            lambda acc, _: (acc[1], acc[0] + acc[1]),
            range(3, n + 1),
            (1, 2),
        )
        return prev1