func partition(s string) [][]string {
    res := [][]string{}
    temp := []string{}

    var recurse func(int)
    recurse = func(index int) {
        if index >= len(s) {
            // make a copy of temp
            cur := make([]string, len(temp))
            copy(cur, temp)
            res = append(res, cur)
            return
        }
        for i := index; i < len(s); i++ {
            if isPali(s, index, i) {
                temp = append(temp, s[index:i+1])
                recurse(i + 1)
                temp = temp[:len(temp)-1]    // backtrack
            }
        }
    }

    recurse(0)
    return res
}

func isPali(s string, l, r int) bool {
    for l < r {
        if s[l] != s[r] {
            return false
        }
        l++
        r--
    }
    return true
}