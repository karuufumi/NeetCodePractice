class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charcount = {}
        left = 0
        n = len(s)
        maxcount = 0
        longest=0
        for right in range (0, n):
            charcount[s[right]] = charcount.get(s[right],0)+1
            maxcount = max(maxcount, charcount[s[right]])
            if right-left+1-maxcount > k:
                charcount[s[left]] -= 1
                left += 1
            longest = max(longest, right-left+1)    
        return longest
