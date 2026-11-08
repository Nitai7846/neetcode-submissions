#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool isPalindrome(const string& s) {
    string rev = s;
    reverse(rev.begin(), rev.end());
    return s == rev;
}

void dfs(int i, const string& s,
         vector<string>& subset,
         vector<vector<string>>& ans) {

    int n = s.size();

    if (i == n) {
        ans.push_back(subset);
        return;
    }

    for (int j = i; j < n; j++) {

        string curr = s.substr(i, j - i + 1);

        if (isPalindrome(curr)) {
            subset.push_back(curr);
            dfs(j + 1, s, subset, ans);
            subset.pop_back();
        }
    }
}

class Solution {
public:
    vector<vector<string>> partition(string s) {

        vector<vector<string>> ans;
        vector<string> subset;

        dfs(0, s, subset, ans);

        return ans;
    }
};