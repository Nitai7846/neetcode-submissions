class Solution {
public:

    string encode(vector<string>& strs) {

        string res = "";

        for (const string& s : strs) {
            res += to_string(s.length()) + "#" + s;
        }

        return res;
    }

    vector<string> decode(string s) {

        vector<string> ans;
        int i = 0;

        while (i < s.length()) {

            int j = i;

            while (s[j] != '#') {
                j++;
            }

            int str_len = stoi(s.substr(i, j - i));

            i = j + 1;
            j = i + str_len;

            ans.push_back(s.substr(i, str_len));

            i = j;
        }

        return ans;
    }
};



