func numOfSubarrays(arr []int, k int, threshold int) int {

	hashSet := make(map[int]int)

	// for _, num := range arr{
	// 	hashSet[num] = true
	// }

	l := 0 
	count := 0
	res := 0

	for r := 0; r < len(arr); r++{

		hashSet[arr[r]]++
		count++
		avg := 0

		if count == k {

			for k, v := range hashSet {
				avg += k*v 
			}
			avg = avg/k

			if avg >= threshold {
				res ++
			}
			hashSet[arr[l]]--
			l++
			count--
			
		}

	}

	return res

}
