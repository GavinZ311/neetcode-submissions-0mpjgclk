class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, r, c, visit):
            row, col = len(grid), len(grid[0])

            if r == row or c == col or min(r,c) < 0 or grid[r][c] == 1 or (r, c) in visit:
                return 0
            
            if r == row-1 and c == col-1:
                return 1
            
            visit.add((r,c))
            count = 0

            count += dfs(grid, r+1, c, visit)
            count += dfs(grid, r-1, c, visit)
            count += dfs(grid, r, c+1, visit)
            count += dfs(grid, r, c-1, visit)

            visit.remove((r,c))
            return count
        
        return dfs(grid, 0, 0, set())