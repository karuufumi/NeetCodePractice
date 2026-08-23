class Solution:
    def isHappy(self, n: int) -> bool:
        
        hashTB = set()
        while (n!=1):
            if n in hashTB:
                return False
            hashTB.add(n)
            tmp = 0
            while (n>0):
                tmp += (n%10)**2
                n //=10
            n = tmp
        return True