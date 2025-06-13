class Solution:
    visited = set()
    m = 0
    n = 0

    def dfs(self, grid: List[List[str]], r: int, c: int):
        m = self.m
        n = self.n

        # Base case
        if(
            r < 0 or r > m-1 or
            c < 0 or c > n-1 or
            grid[r][c] == "0" or
            (r,c) in self.visited
        ):
            return 0
        else:
            # print(f"VALID DFS AT: {r},{c}")
            # print(f"R:{r}, C:{c}, Visited:{self.visited}, Grid val:{grid[r][c]}")
            self.visited.add((r,c))
            self.dfs(grid, r+1, c)
            self.dfs(grid, r-1, c)
            self.dfs(grid, r, c+1)
            self.dfs(grid, r, c-1)
            return 1

    def numIslands(self, grid: List[List[str]]) -> int:

        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = set() # Each testcase runs on the same object so have to reset to empty set

        m = self.m
        n = self.n

        island_count = 0

        for i in range(m):
            for j in range(n):
                print(i,j)
                ctr = self.dfs(grid, i, j)
                if ctr == 1:
                    print(f"VALID DFS AT: {i},{j}")
                island_count = island_count + ctr

        return island_count
