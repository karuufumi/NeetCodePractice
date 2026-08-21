class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i,j,max_= 0,0,0
        hashTB = set()
        #hashTB.add(s[i])
        while j < len(s): 
            while s[j] in hashTB and i < j:
                hashTB.discard(s[i])
                i=i+1
            hashTB.add(s[j])
            max_ = max(max_,j-i+1)
            j= j +1
        return max_