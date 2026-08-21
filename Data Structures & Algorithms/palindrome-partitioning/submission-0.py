class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        tmp = []

        def dfs(i):
            if i == len(s):
                res.append(tmp.copy())
                return

            for end in range(i, len(s)):
                sub = s[i:end+1]

                if sub == sub[::-1]:
                    tmp.append(sub)
                    dfs(end+1)
                    tmp.pop()
            
        dfs(0)
        return res
        