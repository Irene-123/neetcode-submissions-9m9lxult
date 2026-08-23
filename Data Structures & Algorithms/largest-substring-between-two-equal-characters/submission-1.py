class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        ans = -1

        for index, c in enumerate(s):
            if c in seen:
                ans = max(ans, index - seen[c] -1)
            else:
                seen[c] = index

        return ans


            