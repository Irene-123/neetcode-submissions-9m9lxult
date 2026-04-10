func minSubArrayLen(target int, nums []int) int {

	l := 0
	res := len(nums)+1
	sum := 0

	for r := 0; r < len(nums); r++ {

		sum += nums[r]

		for sum >= target {

			res = min(res, r - l+1)

			sum -= nums[l]
			l++
		}


	}

	if res != len(nums) + 1 {
		return res
	} else {
		return 0
	}

}
