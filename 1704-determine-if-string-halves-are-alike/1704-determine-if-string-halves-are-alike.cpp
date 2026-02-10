class Solution {
public:
    bool halvesAreAlike(string s) {
        auto isVowel = [](char c) {
            c = tolower(c);
            return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
        };

        int n = s.size(), cnt = 0;
        for (int i = 0; i < n / 2; i++) {
            cnt += isVowel(s[i]);
            cnt -= isVowel(s[i + n / 2]);
        }
        return cnt == 0;
    }
};
