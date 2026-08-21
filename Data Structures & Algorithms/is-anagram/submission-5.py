class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_,t_ = sorted(s), sorted(t)
        return len(s_) == len(t_) and all(i == j for i,j in zip(s_,t_))