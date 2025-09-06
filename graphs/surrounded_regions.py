from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIRS = [(0,1), (0,-1), (1,0), (-1,0)]
        ROWS, COLS = len(board), len(board[0])
        edges = set()
        
        for c in range(COLS):
            edges.add((0,c))
            edges.add((ROWS-1,c))
        for r in range(ROWS):
            edges.add((r, 0))
            edges.add((r, COLS-1))
        

        invalid = set() # Coordinates for regions that shouldn't be flipped
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and ((nr,nc) not in invalid) and (board[nr][nc] == "O"):
                        invalid.add((nr,nc))
                        q.append((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) in edges:
                    invalid.add((r,c))
                    bfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in invalid:
                    board[r][c] = 'X'
