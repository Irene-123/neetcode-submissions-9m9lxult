class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp))
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        ans = ""
        values = self.timemap[key]
        left, right = 0, len(values)

        while left < right: # Return value with largest timestamp 
            mid = left + (right - left)//2 

            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                left = mid + 1
            else:
                right = mid 

        return ans

        
