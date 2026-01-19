class Solution {
    private int m, n, threshold;
    private int[][] s;
    
    public int maxSideLength(int[][] mat, int threshold) {
        m = mat.length;
        n = mat[0].length;
        this.threshold = threshold;
        
        // Build prefix sum array
        s = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + mat[i-1][j-1];
            }
        }
        
        // Binary search
        int left = 0, right = Math.min(m, n);
        while (left < right) {
            int mid = (left + right + 1) >> 1;
            if (check(mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
    
    private boolean check(int k) {
        for (int i = 0; i <= m - k; i++) {
            for (int j = 0; j <= n - k; j++) {
                int sum = s[i+k][j+k] - s[i][j+k] - s[i+k][j] + s[i][j];
                if (sum <= threshold) return true;
            }
        }
        return false;
    }
}
