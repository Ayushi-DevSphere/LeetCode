class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        long double totalArea = 0;
        long double low = 1e18, high = -1e18;

        // Compute total area and bounds
        for (auto &sq : squares) {
            long double y = sq[1];
            long double l = sq[2];
            totalArea += l * l;
            low = min(low, y);
            high = max(high, y + l);
        }

        long double target = totalArea / 2.0;

        // Binary search
        for (int i = 0; i < 80; i++) {
            long double mid = (low + high) / 2.0;
            long double areaBelow = 0;

            for (auto &sq : squares) {
                long double y = sq[1];
                long double l = sq[2];

                if (mid > y) {
                    areaBelow += min(mid - y, l) * l;
                }
            }

            if (areaBelow < target)
                low = mid;
            else
                high = mid;
        }

        return (double)((low + high) / 2.0);
    }
};
