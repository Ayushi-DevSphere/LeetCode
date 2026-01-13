class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        long double total = 0;
        long double minY = LLONG_MAX;
        long double maxY = LLONG_MIN;
        
        for (auto &sq : squares) {
            long double y = sq[1];
            long double l = sq[2];
            total += l * l;
            minY = min(minY, y);
            maxY = max(maxY, y + l);
        }

        long double half = total / 2.0;
        long double low = minY, high = maxY;

        for (int it = 0; it < 80; ++it) {
            long double mid = (low + high) / 2.0;
            long double areaBelow = 0.0;

            for (auto &sq : squares) {
                long double y = sq[1];
                long double l = sq[2];
                if (mid <= y) {
                } else if (mid >= y + l) {
                    areaBelow += l * l;
                } else {
                    areaBelow += (mid - y) * l;
                }
            }

            if (areaBelow < half) {
                low = mid;
            } else {
                high = mid;
            }
        }

        return (double)((low + high) / 2.0);
    }
};
