from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        answer = []
        maxCandies = max(candies)
        print(maxCandies)

        for c in candies:
            if c + extraCandies >= maxCandies:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer

# Test case
solution = Solution()
s = [2,3,5,1,3]
extra = 3
print(solution.kidsWithCandies(s, extra))