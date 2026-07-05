func twoSum(numbers []int, target int) []int {

	temp := 0
	i := 0
	j := len(numbers) - 1

	for i < j {

		temp = numbers[i] + numbers[j]
		if temp > target {
			j --
		} else if temp < target {
			i ++
		} else {
			return []int{i+1, j+1}
		}
	}

	return []int{-1, -1}

}
