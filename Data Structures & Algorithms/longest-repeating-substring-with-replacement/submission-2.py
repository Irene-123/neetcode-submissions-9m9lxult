class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        i = 0
        max_freq = 0
        ans = 0
        mp = collections.defaultdict(int)

        for j in range(0, n):
            mp[s[j]] += 1
            max_freq = max(max_freq, mp[s[j]])

            while (j - i + 1) - max_freq > k:
                mp[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

        return ans

            
