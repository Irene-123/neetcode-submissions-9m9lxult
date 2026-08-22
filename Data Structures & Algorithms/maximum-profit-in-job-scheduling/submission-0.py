class Solution:

    def recurse(self, jobs, index):
        
        if index == 0:
            return jobs[index][2]

        if index < 0:
            return 0

        if index in self.dp:
            return self.dp[index]
        
        # print(index)
        skip = self.recurse(jobs, index-1)
        
        starttime = jobs[index][0]
        start, end = 0, index

        last_job_index = -1

        while start < end:
            mid = start + (end - start)//2

            if jobs[mid][1] <= starttime:
                start = mid + 1
                last_job_index = mid
            else:
                end = mid
        
        # print("At Index", index, "Last Job Index", last_job_index)
        taken = jobs[index][2]
        if last_job_index != -1:
            taken += self.recurse(jobs, last_job_index)

        self.dp[index] = max(skip, taken)
        return self.dp[index]


    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        self.dp = {}

        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs = sorted(jobs, key = lambda x: (x[1], x[0]))
        # print(jobs)
        
        # Essence : at ith Max profit = 
        # Take a Job ith + best previous job (ending at ith)
        # Don't take it, Skip

        return self.recurse(jobs, n-1)

        