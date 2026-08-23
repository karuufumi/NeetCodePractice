class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = digits[::-1]

        for i in range(len(tmp)):
            if tmp[i] < 9:
                tmp[i] += 1
                return tmp[::-1]

            tmp[i] = 0

        tmp.append(1)
        return tmp[::-1]