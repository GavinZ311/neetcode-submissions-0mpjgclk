class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotted = set()
        queue = deque()
        time = 0
        fresh_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    rotted.add((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or (nr, nc) in rotted or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    rotted.add((nr, nc))
                    fresh_count -= 1

            time += 1

        return time if fresh_count == 0 else -1
                                
                

        