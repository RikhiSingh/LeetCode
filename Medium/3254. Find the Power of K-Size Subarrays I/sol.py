from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        answer = []
        left = 0
        consecutive = 1
        
        for right in range(len(nums)):
            if right > 0 and nums[right-1] + 1 == nums[right]:
                consecutive += 1
                
            if right - left + 1 > k:
                if nums[left] +1 == nums[left+1]:
                    consecutive -= 1
                left += 1
                
            if right - left + 1 == k:
                if consecutive == k:
                    answer.append(nums[right])
                else:
                    answer.append(-1) 
                
        return answer
        
        
    
# Test case
solution = Solution()
s = [2,2,2,2,2]
k = 4
print(solution.resultsArray(s, k))