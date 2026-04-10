func characterReplacement(s string, k int) int {
	mp := make(map[byte]int)
	res := 0
	l := 0
	maxf := 0

	for r := 0; r < len(s); r++ {

		mp[s[r]]++
		maxf = max(maxf, mp[s[r]])

		for (r - l + 1) - maxf > k {

			mp[s[l]]--
			l++

		}

		res = max(res, r - l + 1)
	}

	return res

}
