class Solution:
    def isValid(self, i, j, m, n):
        if i < 0 or i >= m:
            return False
        if j < 0 or j >= n:
            return False
        return True

    def dfs(self, i, j, vis, grid):
        m = len(grid)
        n = len(grid[0])
        if not self.isValid(i, j, m, n):
            return 0
        if vis[i][j]:
            return 0
        if grid[i][j] == 0:
            return 0
        vis[i][j] = True
        return (1 + self.dfs(i-1, j, vis, grid)
                  + self.dfs(i+1, j, vis, grid)
                  + self.dfs(i, j-1, vis, grid)
                  + self.dfs(i, j+1, vis, grid))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[False] * n for _ in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 1:
                    area = self.dfs(i, j, vis, grid)
                    max_area = max(area, max_area)
        return max_area
        