#include <vector>
#include <string>
using namespace std;

bool isValid(int i, int j, int m, int n) {
    if (i < 0 || i >= m)
        return false;

    if (j < 0 || j >= n)
        return false;

    return true;
}

bool dfs(int i, int j, int m, int n, int curr_len,
         vector<vector<char>>& board,
         string& word,
         vector<vector<bool>>& vis) {

    if (!isValid(i, j, m, n))
        return false;

    if (vis[i][j])
        return false;

    if (board[i][j] != word[curr_len])
        return false;

    if (curr_len == word.size() - 1)
        return true;

    vis[i][j] = true;

    bool found = (
        dfs(i + 1, j, m, n, curr_len + 1, board, word, vis) ||
        dfs(i - 1, j, m, n, curr_len + 1, board, word, vis) ||
        dfs(i, j + 1, m, n, curr_len + 1, board, word, vis) ||
        dfs(i, j - 1, m, n, curr_len + 1, board, word, vis)
    );

    vis[i][j] = false;

    return found;
}

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {

        int m = board.size();
        int n = board[0].size();

        vector<vector<bool>> vis(m, vector<bool>(n, false));

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (board[row][col] == word[0]) {
                    if (dfs(row, col, m, n, 0, board, word, vis))
                        return true;
                }
            }
        }

        return false;
    }
};