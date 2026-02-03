class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> mp1;
        unordered_map<string, char> mp2;

        stringstream ss(s);
        string word;
        int i = 0;

        while (ss >> word) {
            if (i >= pattern.size()) return false;

            char c = pattern[i];
            if (mp1.count(c) && mp1[c] != word) return false;
            if (mp2.count(word) && mp2[word] != c) return false;

            mp1[c] = word;
            mp2[word] = c;
            i++;
        }
        return i == pattern.size();
    }
};
