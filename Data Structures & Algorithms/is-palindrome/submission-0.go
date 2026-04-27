func isAlphaNum(c byte) bool {
    return ('A' <= c && c <= 'Z') ||
           ('a' <= c && c <= 'z') ||
           ('0' <= c && c <= '9')
}
func toLowerByte(c byte) byte {
    if 'A' <= c && c <= 'Z' {
        return c + 32
    }
    return c
}

func isPalindrome(s string) bool {

	l, r := 0, len(s)-1
	for l < r {
		// skip non-alphanumeric on left
		for l < r && !isAlphaNum(s[l]) {
			l++
		}
		// skip non-alphanumeric on right
		for r > l && !isAlphaNum(s[r]) {
			r--
		}
		// compare
		if toLowerByte(s[l]) != toLowerByte(s[r]) {
			return false
		}
		l++
		r--
	}
	return true
}
