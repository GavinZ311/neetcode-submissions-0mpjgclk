class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix)*len(matrix[0])-1
        while l <= r:
            mid = (l+r)//2
            cols = len(matrix[0])

            row = mid // cols
            col = mid % cols
            
            val = matrix[row][col]
            
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
        return False