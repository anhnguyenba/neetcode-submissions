class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, index):
            if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or board[r][c] != word[index]:
                return False
            
            if index == len(word) - 1:
                return True

            board[r][c] = '#'

            if dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) \
                or dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1):
                return True
            
            board[r][c] = word[index]
            return False
        
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
                    