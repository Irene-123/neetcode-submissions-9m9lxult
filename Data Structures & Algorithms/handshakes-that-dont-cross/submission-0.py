from functools import cache

class Solution:
    MOD = 10**9 + 7

    @cache
    def numberOfWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 2:
            return 1

        ans = 0

        for i in range(2, n + 1, 2):
            ans += self.numberOfWays(i - 2) * self.numberOfWays(n - i)
            ans %= self.MOD

        return ans