func productExceptSelf(nums []int) []int {

	n := len(nums)
	left := make([]int, n)
	right := make([]int, n)
	res := make([]int, n)

	left[0] = nums[0] 
	right[n-1] = nums[n-1]

	for i := 1; i < n; i++ {
		left[i] = left[i-1] * nums[i]
	}
	for i := n-2; i >=0; i-- {
		right[i] = right[i+1] * nums[i]
	}

	for i := 0; i < n; i++ {

		if i == 0 {
			res[i] = right[i+1]
		} else if i == n-1 {
			res[i] = left[i-1]
		} else {
			res[i] = left[i-1]*right[i+1]
		}

		
	}

	return res
}
