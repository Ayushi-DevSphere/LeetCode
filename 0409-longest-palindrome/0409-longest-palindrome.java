class Solution {
    public int longestPalindrome(String s) {
        int[] freq = new int[128];
        for (char c : s.toCharArray()) {
            freq[c]++;
        }

        int length = 0;
        boolean oddUsed = false;

        for (int f : freq) {
            length += (f / 2) * 2;
            if (f % 2 == 1) oddUsed = true;
        }

        if (oddUsed) length += 1;
        return length;
    }
}
