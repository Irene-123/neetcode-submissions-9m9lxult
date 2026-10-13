class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        n = len(s)
        ans = 0

        i = 0
        for j in range(n):
            while s[j] in mp:
                del mp[s[i]]
                i += 1

            ans = max(ans, j - i + 1)   
            mp[s[j]] = j
        
        return ans
        
