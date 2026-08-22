class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        passengers = {}
        ans = 0
        for trip in trips:
            if trip[1] not in passengers:
                passengers[trip[1]] = 0
            if trip[2] not in passengers:
                passengers[trip[2]] = 0
            
            passengers[trip[1]] += trip[0]
            passengers[trip[2]] -= trip[0]

        print(passengers)

        for i in range(1000):
            if i in passengers:
                capacity -= passengers[i]
            if capacity < 0:
                return False

        return True

        
