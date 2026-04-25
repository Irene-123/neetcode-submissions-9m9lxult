func numIslands(grid [][]byte) int {
    n := len(grid)
    m := len(grid[0])
    
    // Initialize visited array
    vis := make([][]bool, n)
    for i := range vis {
        vis[i] = make([]bool, m)
    }
    
    count := 0

    var dfs func(i, j int)
    dfs = func(i, j int) {
        // Mark current cell as visited
        vis[i][j] = true
        
        // Check all 4 directions
        directions := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
        for _, dir := range directions {
            ni, nj := i + dir[0], j + dir[1]
            if ni >= 0 && ni < n && nj >= 0 && nj < m && 
               grid[ni][nj] == '1' && !vis[ni][nj] {
                dfs(ni, nj)
            }
        }
    }

    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == '1' && !vis[i][j] {
                count++
                dfs(i, j)
            }
        }
    }

    return count
}