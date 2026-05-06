func search(nums []int, target int) int {
    l, r := 0, len(nums)-1

    for l < r {
        m := (l + r) / 2
        if nums[m] > nums[r] {
            l = m + 1
        } else {
            r = m
        }
    }

    pivot := l
    l, r = 0, len(nums)-1

    if target >= nums[pivot] && target <= nums[r] {
        l = pivot
    } else {
        r = pivot - 1
    }

    for l <= r {
        m := (l + r) / 2
        if nums[m] == target {
            return m
        } else if nums[m] < target {
            l = m + 1
        } else {
            r = m - 1
        }
    }

    return -1
}