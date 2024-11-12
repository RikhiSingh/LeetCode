from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []
        
        for a in asteroids:
            while answer and a < 0 < answer[-1]:
                if -a > answer[-1]:
                    answer.pop()
                    continue
                elif -a == answer[-1]:
                    answer.pop()
                break
            else:
                answer.append(a)
                    
        return answer

# Test case
solution = Solution()
s = [5,10,-5]
print(solution.asteroidCollision(s))