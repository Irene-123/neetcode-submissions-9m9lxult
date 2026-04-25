func maxAreaOfIsland(grid [][]int) int {

	n := len(grid)
	if n == 0 {
		return 0
	}
	m := len(grid[0])
	maxArea := 0

	vis := make([][]bool, n)
	for i := range vis {
		vis[i] = make([]bool, m)
	}
    
	var dfs func(i, j int) int
    dfs = func(i, j int) int {

		 if i < 0 || i >= n || j < 0 || j >= m || 
           grid[i][j] == 0 || vis[i][j] {
            return 0
        }
        
        vis[i][j] = true
        area := 1            
        directions := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
        for _, dir := range directions {
            ni, nj := i + dir[0], j + dir[1]
            area += dfs(ni, nj)     
        }
        return area
    }

	for i := 0; i < n; i++{
		for j := 0; j < m; j++ {

			if !vis[i][j] && grid[i][j] == 1 {
				area := dfs(i, j)
				maxArea = max(area, maxArea)
			}
		}
	}
	return maxArea


}
