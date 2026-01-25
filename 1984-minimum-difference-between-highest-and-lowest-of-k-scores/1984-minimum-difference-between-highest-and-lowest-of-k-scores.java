class Solution {
    public int minimumDifference(int[] nums, int k) {
        // Sort the array in ascending order
        Arrays.sort(nums);
        
        // Initialize minimum difference with a large value
        int minDifference = 100000;
        
        // Iterate through all possible windows of size k
        for (int i = 0; i <= nums.length - k; i++) {
            // Calculate difference between max and min in current window
            int currentDifference = nums[i + k - 1] - nums[i];
            
            // Update minimum difference
            minDifference = Math.min(minDifference, currentDifference);
        }
        
        return minDifference;
    }
}
