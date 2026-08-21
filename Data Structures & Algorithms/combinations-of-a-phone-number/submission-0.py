class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        index = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        tmp = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(tmp))
                return
            for j in index[digits[i]]:
                tmp.append(j)
                dfs(i + 1)
                tmp.pop()
        dfs(0)
        return res