from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for f in range(len(flowerbed)):
            # curent is 0
            #                       if first index or if previous is 0
            #                                                           if last or next is 0
            if flowerbed[f] == 0 and (f == 0 or flowerbed[f-1] == 0) and (f == len(flowerbed) - 1 or flowerbed[f+1] ==0):
                flowerbed[f] = 1
                n = n-1
                if n == 0:
                    return True
        return False
        
# Test case
solution = Solution()
s = [1,0,0,0,1]
n = 1
print(solution.canPlaceFlowers(s, n))