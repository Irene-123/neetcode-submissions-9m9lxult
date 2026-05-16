from collections import defaultdict

class TimeMap:

    def __init__(self):
        # Key, value, and timestamp
        # O(1) -> set()
        # O(logn) -> Get Key, timestamp <= prev_timestamp (closest) 
        # using a dict for key. Set takes O(1) to store
        # key: (timestamp, value)
        self.data_store = defaultdict() 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data_store:
            self.data_store[key] = [] 
        self.data_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data_store:
            return ""
        
        value_list = self.data_store[key]
        n = len(value_list)
        start, end = 0, n - 1
        ans = ""
        while start <= end:
            mid = start + (end - start)//2
            if value_list[mid][0] <= timestamp:
                ans = value_list[mid][1] 
                start = mid + 1
            else:
                end = mid -1

        return ans 





        
