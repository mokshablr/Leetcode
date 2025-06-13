class Solution:
    m = 0
    n = 0

    def edge_dfs(self, board, r, c):
        m = self.m
        n = self.n

        #Base case
        if(
            r < 0 or r > m-1 or
            c < 0 or c > n-1 or
            board[r][c] != "O"
        ):
            return board

        else:
            board[r][c] = "Edge"
            board = self.edge_dfs(board, r+1, c)
            board = self.edge_dfs(board, r-1, c)
            board = self.edge_dfs(board, r, c+1)
            board = self.edge_dfs(board, r, c-1)
            return board

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        self.m = m
        self.n = n

        for i in range(m):
            for j in range(n):
                if(
                    i == 0 or
                    i == m-1 or
                    j == 0 or
                    j == n-1
                ):
                    if board[i][j] == "O":
                        board = self.edge_dfs(board, i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "Edge":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
