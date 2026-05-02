func trap(height []int) int {

    ans := 0
    n := len(height)
    left_max := make([]int, n)
    right_max := make([]int, n)
    left_max[0], right_max[n-1] = height[0], height[n-1]

    for i := 1; i < n; i++{
        left_max[i] = max(height[i], left_max[i-1])
    }
    for i := n-2; i >=0; i-- {
        right_max[i] = max(height[i], right_max[i+1])
    }

    for i := 0; i < n; i++{
        ans += min(left_max[i], right_max[i]) - height[i]
    }

    return ans
}
