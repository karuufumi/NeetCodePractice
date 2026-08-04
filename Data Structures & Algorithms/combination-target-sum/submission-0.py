class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cur: List[int], total: int):
            if total == target:
                res.append(cur[::])
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])   # choose candidates[i]
            cur.pop()
            dfs(i + 1, cur, total)              # skip candidates[i]

        dfs(0, [], 0)
        return res