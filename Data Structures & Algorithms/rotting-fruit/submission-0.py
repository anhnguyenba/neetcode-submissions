class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        freshes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshes += 1
        
        minutes = 0
        while queue and freshes > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nei_r, nei_c = r + dr, c + dc
                    if 0 <= nei_r < ROWS and 0 <= nei_c < COLS and grid[nei_r][nei_c] == 1:
                        grid[nei_r][nei_c] = 2
                        queue.append((nei_r, nei_c))
                        freshes -= 1
            minutes += 1

        return minutes if freshes == 0 else -1

                    
