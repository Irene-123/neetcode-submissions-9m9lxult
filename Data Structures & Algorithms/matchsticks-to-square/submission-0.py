import collections 

class Solution:
    def recurse(self, index, matchsticks):
        if index >= len(matchsticks):
            return True

        # 0, 0, 0, 0
        # 4, 4, 4, 4
        # print(self.sides)
        ans = True
        if self.dp[index]:
            return dp[index]

        for i in range(4):
            if self.sides[i] + matchsticks[index] <= self.size:
                self.sides[i] += matchsticks[index]
                ans = self.recurse(index + 1, matchsticks)
                if ans:
                    self.dp[index] = True
                    return True
                self.sides[i] -= matchsticks[index]

        self.dp[index] = False
        return False
        
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks)%4 != 0 or len(matchsticks) < 4:
            return False 
        self.dp = collections.defaultdict(int)
        self.size = sum(matchsticks)//4
        matchsticks.sort(reverse = True)
        # 4, 4, 3, 2, 2, 1
        # 5, 4, 4, 1, 1, 1
        self.sides = [0]*4
        self.sticks = 0
        ans = self.recurse(0, matchsticks)

        return ans 

        