func findMaxConsecutiveOnes(nums []int) int {
	n := len(nums)
	i, j, zeros := 0, 0, 0
	maxL := 0

	for j = 0; j < n; j++{

		if nums[j] == 0 {
			zeros += 1
		}

		for zeros > 1  {
			if nums[i] == 0 {
				zeros--
			}
			i++
			
		}
		maxL = max(maxL, j - i + 1)

	}

	return maxL

}
