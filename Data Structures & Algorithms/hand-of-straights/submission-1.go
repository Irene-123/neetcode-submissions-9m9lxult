func isNStraightHand(hand []int, groupSize int) bool {

	m := make(map[int]int) 

	for _, num := range hand {
		m[num]++
	}

	keys := make([]int, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	// 1, 2, 2, 3, 3, 4, 4, 5

	for _, num := range keys {

		curr := num
		for m[curr] > 0 {
			for i := 0; i < groupSize; i++ {
				new_curr := curr + i 
				if m[new_curr] == 0 {
					return false
				}
				m[new_curr]--
			}
		}
		

		
	}

	return true
	
    
}
