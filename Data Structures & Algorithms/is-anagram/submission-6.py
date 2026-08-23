class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable1 = {chr(c) : 0 for c in range(ord('a'),ord('z')+1)}
       # hashTable2 = {chr(c) : 0 for c in range(ord('a'),ord('z')+1)}
        for c in s:
            hashTable1[c] += 1
        for c in t:
            hashTable1[c] -=1
        for i in hashTable1.values():
            if i !=0:
                return False
        
        return True