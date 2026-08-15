class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix : return False
        m = len(matrix[0])
        for it in matrix:
            temp_len=len(it) 
            if m and target>it[temp_len -1 ]:
                continue 
            else:
                l=0
                r= temp_len
                while l<r:
                    mid= l+ ((r-l)//2)
                    if it[mid] <target:
                        l+=1
                    elif it[mid] >target:
                        r -=1
                    elif it[mid] == target:
                        return True
        return False