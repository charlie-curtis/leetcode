class Solution {
    public long countQuadruplets(int[] nums) {

        //have to code this in java because the LC problem setters chose n=4000 for an O(N^2) solution.
        //This means it'll only pass in certain languages or minor optimizations
        //The standard O(N^2) solution is N=1000 in size
        int n = nums.length;
        int[][] to_left = new int[n][n+1];
        int[][] to_right = new int[n][n+1];

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n+1; j++) {
                to_left[i][j] = to_left[i-1][j];
                if (j > nums[i-1]) {
                    to_left[i][j]+=1;
                }
            }
        }

        for (int i = n-2; i >= 0; i--) {
            for (int j = 1; j < n+1; j++) {
                to_right[i][j] = to_right[i+1][j];
                if (j < nums[i+1]) {
                    to_right[i][j]+=1;
                }
            }
        }

        long ans = 0;
        for (int j = 0; j < n; j++) {
            for (int k = j+1; k < n; k++) {
                if (nums[k] < nums[j]) {
                    long a = to_left[j][nums[k]];
                    long b = to_right[k][nums[j]];
                    ans+=a*b;
                }
            }
        }

        return ans;
        
    }
}