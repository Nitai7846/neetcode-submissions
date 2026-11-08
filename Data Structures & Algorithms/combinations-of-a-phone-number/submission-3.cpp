#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

void dfs(int i, const string& digits,
         unordered_map<char, string>& mapping,
         string& subset,
         vector<string>& ans) {

    if (i == digits.size()) {
        ans.push_back(subset);
        return;
    }

    for (char ch : mapping[digits[i]]) {
        subset.push_back(ch);
        dfs(i + 1, digits, mapping, subset, ans);
        subset.pop_back();
    }
}

class Solution {
public:
    vector<string> letterCombinations(string digits) {

        unordered_map<char, string> mapping = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };

        if (digits.empty())
            return {};

        vector<string> ans;
        string subset = "";

        dfs(0, digits, mapping, subset, ans);

        return ans;
    }
};
