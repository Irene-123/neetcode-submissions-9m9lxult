func climbStairs(n int) int {

	if (n <= 1) {
		return 1
	}

	prev1, prev2 := 1, 2 

	for i := 3; i <=n; i++{
		curr := prev1 + prev2 
		prev1 = prev2
		prev2 = curr
	}

	return prev2


    
}
