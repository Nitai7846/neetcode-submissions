class Solution {
public:
    bool isValid(int i, int j, int m, int n) {
        if (i < 0 || i >= m) return false;
        if (j < 0 || j >= n) return false;
        return true;
    }

    void dfs(int i, int j, vector<vector<bool>>& vis, vector<vector<char>>& grid, int m, int n) {
        if (!isValid(i, j, m, n)) return;
        if (vis[i][j]) return;
        if (grid[i][j] == '0') return;

        vis[i][j] = true;

        dfs(i+1, j, vis, grid, m, n);
        dfs(i-1, j, vis, grid, m, n);
        dfs(i, j+1, vis, grid, m, n);
        dfs(i, j-1, vis, grid, m, n);
    }

    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int count = 0;
        vector<vector<bool>> vis(m, vector<bool>(n, false));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!vis[i][j] && grid[i][j] == '1') {
                    count++;
                    dfs(i, j, vis, grid, m, n);
                }
            }
        }
        return count;
    }
};