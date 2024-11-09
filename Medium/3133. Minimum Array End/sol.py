# https://leetcode.com/problems/minimum-array-end?envType=daily-question&envId=2024-11-09
#  this works but leds to time limit exceeded
# cpp solves that

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x

        # we need one less because the first element will be x itslef
        for i in range(n-1):
            result += 1
            # and we OR it guranteing that all the bits are set in result here
            result = result | x

        return result
    
