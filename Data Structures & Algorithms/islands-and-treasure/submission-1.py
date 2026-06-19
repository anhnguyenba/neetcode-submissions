class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue = [(r, c, 0)]
                    seen = set()
                    while queue:
                        r, c, distance = queue.pop(0)
                        seen.add((r, c))

                        if grid[r][c] != 0:
                            grid[r][c] = min(grid[r][c], distance)

                        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        for dr, dc in directions:
                            nei_r, nei_c = r + dr, c + dc
                            if 0 <= nei_r <= ROWS - 1 and 0 <= nei_c <= COLS - 1 and grid[nei_r][nei_c] != -1 and (nei_r, nei_c) not in seen:
                                queue.append((nei_r, nei_c, distance + 1))
