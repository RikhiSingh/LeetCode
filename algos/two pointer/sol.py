from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            sum = nums[l] + nums[r]
            if sum == k:
                return [nums[l+1], nums[r+1]]
            elif sum < k:
                l += 1
            else:
                r -= 1
        
        
    
# Test case
solution = Solution()
s = [5,7,11,18]
k = 18
print(solution.resultsArray(s, k))