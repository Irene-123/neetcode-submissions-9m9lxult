class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = collections.defaultdict(int)
        ans = []
        # xyxxyz
        # mp = {x: [3], y: [4], z:[5], b:[9], i: [10], s: [11], l: [12]}

        for i in range(len(s)):
            mp[s[i]] = i

        start, end_partition = 0, 0
        size = 0

        while start < len(s):
            size += 1
            c = s[start]
            last_occurence = mp[c]

            end_partition = max(end_partition, last_occurence)

            if start == end_partition:
                ans.append(size) 
                size = 0
            start += 1

        return ans



            

            