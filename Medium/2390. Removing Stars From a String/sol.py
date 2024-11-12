class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        
        for char in s:
            if char == "*":
                answer.pop()
            else:
                answer.append(char)
        
        return "".join(answer)
        
        
# Test case
solution = Solution()
s = "leet**cod*e"
print(solution.removeStars(s))