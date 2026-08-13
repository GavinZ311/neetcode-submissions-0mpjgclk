class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            nonlocal max_area
            area = 1
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while q:
                r, c = q.popleft()
                for dr, dc in movements:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        area += 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
            max_area = max(max_area, area)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    bfs(r, c)

        return max_area