func countSubstrings(s string) int {

	n := len(s)
	ans := 0
	dp := make([][]bool, n)
	for row := range dp {
		dp[row] = make([]bool, n)
	}

	for i := n -1; i >=0; i-- {
		for j := i; j < n; j++ {
			if s[i] == s[j] && (j - i <= 2 || dp[i+1][j-1]) {
				dp[i][j] = true
				ans++
			}
		}
	}
	return ans
    
}
