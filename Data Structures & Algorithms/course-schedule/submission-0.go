func canFinish(n int, preq [][]int) bool {

	courseMap := make(map[int][]int)
    visited := make([]bool, n)
    path := make([]bool, n) 

    var dfs func(int) bool

    dfs = func(i int) bool {

        visited[i] = true
        path[i] = true

        for _, node := range courseMap[i] {

            if path[node] == true {
                return false
            } 

            if visited[node] == true {
                continue
            }
            
            if !dfs(node) {
                return false
            }
        }
        path[i] = false
        return true
    }

	for _, p := range preq {
		courseMap[p[0]] = append(courseMap[p[0]], p[1])
	}

    for i := 0; i < n; i++ {
        
        if !visited[i] && !dfs(i) {
            return false
        }
    }

	return true
}