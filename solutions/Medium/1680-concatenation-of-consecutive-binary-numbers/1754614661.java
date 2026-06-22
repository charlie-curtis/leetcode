class Solution {
    public int concatenatedBinary(int n) {
        long ans = 0, cur = 1;
        int MOD = 1000000007;
        
        for (int i = n; i >= 1; i--) {
            String binary = Integer.toBinaryString(i);
            
            for (int j = binary.length() - 1; j >= 0; j--) {
                ans += (binary.charAt(j) - '0') * cur;
                cur <<= 1;
                cur %= MOD;
                ans %= MOD;
            }
        }
        
        return (int) ans;
    }
}