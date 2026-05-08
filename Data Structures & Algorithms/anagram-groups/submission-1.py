class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            hash_key = [0]*26 
            for c in s:
                hash_key[ord(c) - ord('a')] += 1 
            hash_key = tuple(hash_key)
            if hash_key not in mp:
                mp[hash_key] = []
            mp[hash_key].append(s)
        res = []
        for key, value in mp.items():
            res.append(value)
        return res

        