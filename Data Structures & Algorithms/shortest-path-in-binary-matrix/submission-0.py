class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        queue = [(0, 0, 1)]
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        result = sys.maxsize
        while queue:
            r, c, step = queue.pop(0)

            if r == ROWS - 1 and c == COLS - 1:
                result = min(result, step)

            for d in directions:
                next_r, next_c = r + d[0], c + d[1]

                if next_r < 0 or next_r >= ROWS or next_c < 0 or next_c >= COLS:
                    continue

                if grid[next_r][next_c] != 1 and (next_r, next_c) not in visited:
                    queue.append((next_r, next_c, step + 1))
                    visited.add((next_r, next_c))
        return result if result < sys.maxsize else -1

