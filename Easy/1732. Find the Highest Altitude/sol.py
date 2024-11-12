from itertools import accumulate
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))
        


# Test case
solution = Solution()
word = [-5,1,5,0,-7]
print(solution.largestAltitude(word))