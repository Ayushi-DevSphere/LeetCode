class Solution {
public:
    int longestConsecutive(vector<int>& arr) {
        if (arr.empty()) return 0;

        sort(arr.begin(), arr.end());
        int longest = 1, curr = 1;

        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] == arr[i - 1] + 1) {
                curr++;
            } else if (arr[i] != arr[i - 1]) {
                curr = 1;
            }
            longest = max(longest, curr);
        }
        return longest;
    }

    int maximizeSquareHoleArea(int n, int m,
                               vector<int>& hBars,
                               vector<int>& vBars) {

        int maxH = longestConsecutive(hBars);
        int maxV = longestConsecutive(vBars);

        int side = min(maxH + 1, maxV + 1);
        return side * side;
    }
};
