class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if len(grid) == 1:
            return 1

        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        length = 1
        visited.add((0, 0))
        queue.append((0, 0))

        while queue:

            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                
                movements = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

                for dr, dc in movements:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            length += 1

        return -1