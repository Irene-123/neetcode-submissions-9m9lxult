class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        result = 0
        prefix = 0
        mp[0] = 1

        for num in nums:
            prefix += num

            remainder = prefix % k

            result += mp[remainder]
            mp[remainder]+= 1
        
        return result