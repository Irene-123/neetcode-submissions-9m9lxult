class Solution {
    public boolean backtrack(int [] matchsticks, int[] sides, int len, int index) {

        if (index == matchsticks.length) {
            return true;
        }

        for (int i = 0; i < 4; i++) {

            if (matchsticks[index] + sides[i] > len) continue;

            sides[i] += matchsticks[index];

            if (backtrack(matchsticks, sides, len, index+1)) return true;

            sides[i] -= matchsticks[index];
        }

        return false;
    }
    public boolean makesquare(int[] matchsticks) {
        // 1 
        // 2 2 
        // 3
        // 4 4

        int n = matchsticks.length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += matchsticks[i];
        }
        if (sum % 4 != 0) return false;
        int len = sum/4;

        int[] sides = new int[4];

        // Conditions for failure: if a matchstick > len 
        // If all 4 sides are not met 
        // 1 2 2 3 4 4

        return backtrack(matchsticks, sides, len, 0);

    }
}