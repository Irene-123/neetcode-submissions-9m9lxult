func minEatingSpeed(piles []int, h int) int {

    // n := len(piles)

    // if n == 1 {
    //     return piles[0]
    // }

    canEat := func(k int) bool {
        
        hours := 0

        for _, p := range(piles) {
            hours += (p + k - 1) / k
        }

        if hours <= h {
            return true
        } 
        return false

    }

    l, r := 1, piles[0]
    for _, pile := range piles {
        if pile > r {
            r = pile
        }
    }
    mid := l

    for l < r {

        mid = l + (r - l) / 2

        if canEat(mid) {
            r = mid
        } else {
            l = mid + 1
        }

    }
    return l
}
