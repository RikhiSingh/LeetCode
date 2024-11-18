from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []

        circular = code * 2
        
        if k == 0:
            answer = [0] * len(code)
            return answer
        elif k > 0:
            answer = [sum(circular[i + 1: i + 1 + k]) for i in range(len(code))]
            return answer
        else:
            k = abs(k)
            answer = [sum(circular[i+(len(code))-k: i+(len(code))]) for i in range(len(code))]
            return answer
    
        
        
    
# Test case
solution = Solution()
s = [5,7,1,4]
k = 0
print(solution.decrypt(s, k))