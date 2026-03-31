func maxArea(heights []int) int {
    i := 0
    j := len(heights) - 1
    res := 0

    for i < j {
        curr := min(heights[i], heights[j])*(j-i)

        if curr > res {
            res = curr
        }

        if heights[i] < heights[j]{
            i += 1
        } else {
            j -=1
        }
    }
    
    
    return res

}
