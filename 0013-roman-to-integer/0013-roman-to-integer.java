class Solution {
    public int romanToInt(String s) {
        int[] val = new int[128];
        val['I'] = 1; val['V'] = 5; val['X'] = 10;
        val['L'] = 50; val['C'] = 100;
        val['D'] = 500; val['M'] = 1000;

        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            int curr = val[s.charAt(i)];
            if (i + 1 < s.length() && curr < val[s.charAt(i + 1)]) {
                sum -= curr;
            } else {
                sum += curr;
            }
        }
        return sum;
    }
}
