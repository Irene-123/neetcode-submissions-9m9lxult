class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {} 
        res = [] 

        for s in strs:
            sorteds = ''.join(sorted(s))
            if sorteds not in d:
                d[sorteds] = [] 
            d[sorteds].append(s)
        
        for k, v in d.items():
            res.append(v) 

        return res



        
        

        