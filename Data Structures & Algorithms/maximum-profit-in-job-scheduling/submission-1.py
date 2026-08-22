class Solution:

    def recurse(self, jobs, index):
        
        if index == len(jobs) - 1:
            return jobs[index][2]

        if index >= len(jobs):
            return 0

        if index in self.dp:
            return self.dp[index]
        
        # print(index)
        skip = self.recurse(jobs, index+1)
        
        endtime = jobs[index][1]
        start, end = index + 1, len(jobs)

        new_job_index = -1

        while start < end:
            mid = start + (end - start)//2

            if jobs[mid][0] >= endtime:
                end = mid
                new_job_index = mid
            else:
                start = mid + 1
        
        print("At Index", index, "new Job Index", new_job_index)
        taken = jobs[index][2]
        if new_job_index != -1:
            taken += self.recurse(jobs, new_job_index)

        self.dp[index] = max(skip, taken)
        return self.dp[index]


    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        self.dp = {}

        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs = sorted(jobs, key = lambda x: (x[0], x[1]))
        print(jobs)

        return self.recurse(jobs, 0)

        