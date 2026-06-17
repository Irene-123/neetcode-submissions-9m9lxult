class Solution:
    def isInterleave(self, s: str, t: str, ans: str) -> bool:

        def recurse(i, j, n, m):

            if abs(n-m) > 1:
                return False
            if i + j >= len(ans):
                return True

            # s = "a" t = "b" ans = "ab"

            if (i,j, n, m) in dp:
                return dp[(i,j, n, m)]

            if i < len(s) and s[i] == ans[i+j]:
                dp[(i,j, n, m)] = recurse(i, j+1, n+1, m) or recurse(i+1, j, n, m)
            elif j < len(t) and t[j] == ans[i+j]:
                dp[(i,j, n, m)] = recurse(i+1, j, n, m+1) or recurse(i, j+1, n, m)
            else:
                dp[(i,j, n, m)] = False

            return dp[(i,j, n, m)]
            
        if len(s) + len(t) != len(ans):
            return False

        # record = (i, j)
        dp = {}

        return recurse(0, 0, 0, 0)
        