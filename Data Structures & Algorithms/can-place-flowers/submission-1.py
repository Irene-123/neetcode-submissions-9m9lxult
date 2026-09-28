class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plots = 0

        # 0, 0, 1, 0, 0, 1
        # 0, 1, 0, 0, 0, 1
        # 1, 0, 0, 1, 0, 1

        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2 
            else:
                if (i < len(flowerbed)-1 and flowerbed[i+1] != 1) or (i == len(flowerbed) - 1 and flowerbed[i-1] != 1):
                    plots += 1
                i += 2
        

        return plots >= n