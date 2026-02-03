class Solution {
    public boolean isTrionic(int[] nums) {
        int n = nums.length;
        
        // A trionic array must have at least 4 elements
        // to satisfy 0 < p < q < n-1 with all three segments non-empty
        if (n < 4) {
            return false;
        }
        
        int i = 0;
        
        // Phase 1: Find the first strictly increasing segment
        while (i < n - 2 && nums[i] < nums[i + 1]) {
            i++;
        }
        
        // If no increasing segment exists (i is still 0), return false
        if (i == 0) {
            return false;
        }
        
        // Phase 2: Find the strictly decreasing segment
        int decreaseStart = i;
        while (i < n - 1 && nums[i] > nums[i + 1]) {
            i++;
        }
        
        // If no decreasing segment exists or we've reached the end, return false
        if (i == decreaseStart || i == n - 1) {
            return false;
        }
        
        // Phase 3: Find the final strictly increasing segment
        while (i < n - 1 && nums[i] < nums[i + 1]) {
            i++;
        }
        
        // Valid trionic pattern if we've reached the end of the array
        return i == n - 1;
    }
}
