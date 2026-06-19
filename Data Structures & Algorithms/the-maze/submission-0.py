class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(r, c):
            # Base case: already visited this stopping point
            if visited[r][c]:
                return False
            
            # Base case: reached destination
            if r == destination[0] and c == destination[1]:
                return True
            
            # Mark as visited
            visited[r][c] = True
            
            # Four directions: up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dr, dc in directions:
                nr, nc = r, c
                
                # Roll in this direction until hitting a wall
                while (0 <= nr + dr < m and 0 <= nc + dc < n and 
                       maze[nr + dr][nc + dc] == 0):
                    nr += dr
                    nc += dc
                
                # If we moved to a new position, explore from there
                if nr != r or nc != c:
                    if dfs(nr, nc):
                        return True
            
            return False
        
        return dfs(start[0], start[1])
