

func longestPalindrome(s string) string {	

	n := len(s) 
	longest_str := ""

	for i := 0; i < n; i++ {

		// old length palindrome
		l := i-1
		r := i+1
		temp := palin(l, r, s)
		if len(longest_str) < len(temp) {
			longest_str = temp
		}
		// even length palindrome
		l = i
		r = i+1
		temp = palin(l, r , s)
		if len(longest_str) < len(temp) {
			longest_str = temp
		}

	}

	return longest_str
}
func palin(l int, r int, s string) string {
	for (l >= 0 && r < len(s)) && (s[l] == s[r]) {
		l--
		r++
	}
	return s[l+1: r]
}
