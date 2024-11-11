# https://leetcode.com/problems/contains-duplicate
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        answer = set()
        
        for num in nums:
            if num in answer:
                return True
            else:
                answer.add(num)
                
        return False
        
solution = Solution()
word1 = [1,2,3,4]
print(solution.containsDuplicate(word1)) 
word1 = [1,2,3,1]
print(solution.containsDuplicate(word1)) 